from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os


API_KEY = os.environ['API_KEY']
API_ENDPOINT = 'https://api.themoviedb.org/3/search/movie'
API_MOVIE_INFO_ENDPOINT = 'https://api.themoviedb.org/3/movie/'
IMG_URL = 'https://image.tmdb.org/t/p/w500'

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///top-10-movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(500))
    img_url = db.Column(db.String(500), nullable=False)


db.create_all()


class RateMovieForm(FlaskForm):
    rating = StringField('Your Rating out of 10 e.g. 6.9', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Submit Changes')


class AddMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating.desc()).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = i + 1
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route('/update', methods=['GET', 'POST'])
def update():
    movie_id = request.args.get('id')
    selected_movie = Movie.query.get(movie_id)
    form = RateMovieForm()
    if form.validate_on_submit():
        selected_movie.rating = float(form.rating.data)
        selected_movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=selected_movie, form=form)


@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    selected_movie = Movie.query.get(movie_id)
    db.session.delete(selected_movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['POST', 'GET'])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        params = {
            'api_key': API_KEY,
            'query': movie_title,
        }
        movies = requests.get(API_ENDPOINT, params).json()['results']
        return render_template('select.html', movies=movies)
    return render_template('add.html', form=form)


@app.route('/selected')
def complete():
    movie_id = request.args.get('movie')
    response = requests.get(f'{API_MOVIE_INFO_ENDPOINT}{movie_id}', {'api_key': API_KEY})
    data = response.json()
    new_movie = Movie(
        title=data['title'],
        year=data['release_date'].split('-')[0],
        description=data['overview'],
        img_url=f'{IMG_URL}{data["poster_path"]}'
    )
    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for('update', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
