import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
import durationMod

# Environmental variables
os.environ['SPOTIPY_CLIENT_ID'] = 'MyClientID'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'MySecret'

# id of Twenty One Pilots
artistId = '3YQKmKGau1PzlVlkL1iodx'
# uri of artist
lz_uri = f'spotify:artist:{artistId}'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
# getting artist's top tracks
tracksResult = spotify.artist_top_tracks(lz_uri)

for track in tracksResult['tracks'][:10]:
	print('track : ' + track['name'])
	print('popularity(0-100) : ' + str(track['popularity']))
	print('audio : ' + track['preview_url'])
	print('duration : ' + durationMod.getDuration(track['duration_ms']))
	print('is explicit : ' + str(track['explicit']))
	print('cover art : ' + track['album']['images'][0]['url'])
	print()