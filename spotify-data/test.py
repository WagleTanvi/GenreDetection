import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
import pandas as pd 
from random import sample

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="f3a52efb14cf42a3840d1c04b283ca91",
                                               client_secret="fda334c722424e84989f5e95a2abf3d4",
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="user-library-read"))

def getTracks(url):
    tracks = []
    response = sp.playlist_items(url,
                                    offset=0,
                                    fields='items.track.id,total',
                                    additional_types=['track'])
    if len(response['items']) == 0:
        return null 

    for item in response['items']:
        tracks.append(item['track']['id'])

    return tracks

playlists = {
    'pop': "https://open.spotify.com/playlist/37i9dQZF1DX5gQonLbZD9s?si=30767127b8f94469",
    'rock': "https://open.spotify.com/playlist/37i9dQZF1DXcF6B6QPhFDv?si=b03e02334d354bf8",
    'classical': "https://open.spotify.com/playlist/37i9dQZF1DWWEJlAGA9gs0?si=96c90b5d91994be8",
    'country': "https://open.spotify.com/playlist/37i9dQZF1DX1lVhptIYRda?si=598d4d9cae29480a"
}

tracks = {}
for genre in playlists: 
    tracks[genre] = getTracks(playlists[genre])

# crop number of tracks 
lens = []
for genre in tracks:
    lens.append(len(tracks[genre]))

size = min(lens)

for genre in tracks: 
    tracks[genre] = sample(tracks[genre], size)

features = []

for genre in tracks: 
    my_dict = sp.audio_features(tracks[genre])
    for dict in my_d  ict: 
        dict["genre"] = genre
    features.extend(my_dict)

df = pd.DataFrame(features)

print(df.head())
print(df.size)
print