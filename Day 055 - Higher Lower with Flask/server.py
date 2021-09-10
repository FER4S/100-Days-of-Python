from flask import Flask
from random import randint

app = Flask(__name__)

rand = randint(0, 9)


@app.route('/')
def main():
    return '<h1>Guess a number between 0 and 9<h1/><br>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:guessed>')
def guess(guessed):
    if guessed == rand:
        return '<h1 style="color: green">You found me<h1/><br>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif guessed > rand:
        return '<h1 style="color: red">Too high, try again!<h1/><br>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return '<h1 style="color: blue">Too low, try again!<h1/><br>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'


if __name__ == '__main__':
    app.run(debug=True)
