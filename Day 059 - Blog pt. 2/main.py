from flask import Flask, render_template
import requests

data = requests.get('https://api.npoint.io/e5cfd85007505a421486').json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', posts=data)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:post_id>')
def posts(post_id):
    post = data[post_id-1]
    return render_template('post.html', post=post)


if __name__ == '__main__':
    app.run(debug=True)
