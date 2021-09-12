from flask import Flask, render_template
import requests


app = Flask(__name__)

response = requests.get('https://api.npoint.io/c37f7c7d97c9c6067326')
data = response.json()

@app.route('/')
def home():
    return render_template("index.html", blog=data)


@app.route('/post/<int:blog_id>')
def blog(blog_id):
    post = data[blog_id-1]
    return render_template('post.html', post=post)



if __name__ == "__main__":
    app.run(debug=True)
