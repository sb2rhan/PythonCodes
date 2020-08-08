import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
import durationMod
from dotenv import load_dotenv
load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

# Environmental variables
os.environ['SPOTIPY_CLIENT_ID'] = CLIENT_ID
os.environ['SPOTIPY_CLIENT_SECRET'] = CLIENT_SECRET


# artistId from Main.py
def getTracksOfArtist(artistId) -> list:
    """
        This function prints tracks of Artists from Spotify.

        Parameters:
            artistId - string with id of Spotify artist
        Returns:
            list of strings
    """
    # strings with tracks
    tracks = []

    # uri of artist
    lz_uri = f'spotify:artist:{artistId}'

    spotify = spotipy.Spotify(
        client_credentials_manager=SpotifyClientCredentials())
    # getting artist's top tracks
    tracksResult = spotify.artist_top_tracks(lz_uri)

    for track in tracksResult['tracks'][:10]:
        tmpTrack = ""
        tmpTrack += 'Track: ' + track['name'] + ' \n'
        tmpTrack += 'Popularity(0-100): ' + str(track['popularity']) + ' \n'
        tmpTrack += 'Audio: ' + str(track['preview_url']) + ' \n'
        tmpTrack += 'Duration: ' + durationMod.getDuration(
                                            track['duration_ms']) + ' \n'
        tmpTrack += 'Is explicit: ' + str(track['explicit']) + ' \n'
        # tmpTrack += 'Cover art: ' + track['album']['images'][0]['url'] + ' \n'
        tracks.append(tmpTrack)

    return tracks
