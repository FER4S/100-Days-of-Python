from flask import Flask, render_template, url_for, redirect, request, flash
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
from collections import Counter
from sklearn.cluster import KMeans
import cv2
import os


UPLOAD_FOLDER = 'static/files'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'xdxdxdxdxd665132135'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
Bootstrap(app)


def img_preprocess(raw):
    image = cv2.resize(raw, (900, 600), interpolation=cv2.INTER_AREA)
    image = image.reshape(image.shape[0] * image.shape[1], 3)
    return image


def rgb_to_hex(rgb_colour):
    hex_colour = "#"
    for i in rgb_colour:
        hex_colour += ("{:02x}".format(int(i)))
    return hex_colour


def analyze(img):
    clf = KMeans(n_clusters=10)
    color_labels = clf.fit_predict(img)
    center_colors = clf.cluster_centers_
    counts = Counter(color_labels)
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colours = [rgb_to_hex(ordered_colors[i]) for i in counts.keys()]

    values = list(counts.values())
    percentages = [value/sum(values)*100 for value in values]

    sorted_hex_colours = [x for _, x in sorted(zip(percentages, hex_colours), key=lambda pair: pair[0])]
    percentages.sort()

    return sorted_hex_colours[::-1], percentages[::-1]


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def home():
    my_dir = "static/files/"
    file_list = [f for f in os.listdir(my_dir)]
    for f in file_list:
        os.remove(os.path.join(my_dir, f))

    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('show_result', name=filename))
    return render_template('index.html')


@app.route('/result/<name>')
def show_result(name):
    img = cv2.imread(f'static/files/{name}')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    processed_img = img_preprocess(img)
    colours, values = analyze(processed_img)
    return render_template('result.html', name=name, colours=colours, values=values)


if __name__ == '__main__':
    app.run(debug=True)

