import sys
sys.path.append("./../../MSTutorials/APIs/")
import spotifyGet as spotG


def getTracksOfArtist(artist_id, requestBox):
    print("Entry is - ", artist_id)
    tracks = spotG.getTracksOfArtist(artist_id)

    for index, track in enumerate(tracks, start=1):
        requestBox.insert('end', f'{index} - {track}\n')
