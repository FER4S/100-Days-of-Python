import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']
OAUTH_AUTHORIZE_URL = 'https://accounts.spotify.com/authorize'
OAUTH_TOKEN_URL = 'https://accounts.spotify.com/api/token'

date = input('Which year do you want to travel to? Type date in this format YYYY-MM-DD: ')
billboard_url = f'https://www.billboard.com/charts/hot-100/{date}'

response = requests.get(billboard_url)
billboard_web_page = response.text

soup = BeautifulSoup(billboard_web_page, 'html.parser')
top_100_songs = [song.get_text() for song in soup.find_all('span', class_='chart-element__information__song')]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt",
        requests_timeout=9999999999999999999999999999999999999
    )
)
user_id = sp.current_user()['id']

song_uris = []
year = date.split('-')[0]
for song in top_100_songs:
    result = sp.search(q=f'track:{song} year:{year}', type='track')
    print(result)
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f'{date} Billboard 100', public=False)
print(playlist)

sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist['id'], tracks=song_uris)
