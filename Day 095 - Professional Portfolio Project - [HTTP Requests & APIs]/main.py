from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

from heroes import heroes_dict, heroes_img

API_ENDPOINT = 'https://api.opendota.com/api/'


class SearchForm(FlaskForm):
    player_id = StringField('Player ID', validators=[DataRequired()])
    submit = SubmitField('Search')


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    form = SearchForm()
    if form.validate_on_submit():
        player_id = form.player_id.data
        return redirect(url_for('player', id=player_id))
    return render_template('index.html', form=form)


@app.route('/player/<int:id>')
def player(id):
    player_id = id
    player_info = requests.get(f'{API_ENDPOINT}players/{player_id}').json()['profile']
    player_wl = requests.get(f'{API_ENDPOINT}players/{player_id}/wl').json()
    recent_matches = requests.get(f'{API_ENDPOINT}players/{player_id}/recentMatches').json()
    top_heroes = requests.get(f'{API_ENDPOINT}players/{player_id}/heroes').json()[:3]
    top_img = [heroes_img[int(hero['hero_id'])] for hero in top_heroes]
    top_heroes = [hero['games'] for hero in top_heroes]
    recent_heroes = [match['hero_id'] for match in recent_matches]
    recent_img = [heroes_img[hero_id] for hero_id in recent_heroes]
    recent_heroes = [heroes_dict[hero_id] for hero_id in recent_heroes]
    return render_template('player.html', player_info=player_info, wl=player_wl, recent=recent_matches,
                           recent_heroes=recent_heroes, img=recent_img, top=top_heroes, top_img=top_img)


if __name__ == '__main__':
    app.run(debug=True)
