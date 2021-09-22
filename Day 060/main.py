from flask import Flask, render_template, request
import requests
import smtplib
import os

gmail = os.environ['EMAIL']
password = os.environ['PASSWORD']

data = requests.get('https://api.npoint.io/e5cfd85007505a421486').json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', posts=data)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        msg = request.form['msg']
        email_msg = f'{name=}\n{email=}\n{phone=}\n{msg=}'
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(gmail, password)
            connection.sendmail(gmail, 'testing_for_python@yahoo.com', f'Subject:New Message!\n\n{email_msg}')
    return render_template('contact.html')


@app.route('/post/<int:post_id>')
def posts(post_id):
    post = data[post_id-1]
    return render_template('post.html', post=post)


if __name__ == '__main__':
    app.run(debug=True)
