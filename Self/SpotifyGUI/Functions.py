import sys
sys.path.append("./../../MSTutorials/APIs/")
import spotifyGet as spotG


def getTracksOfArtist(artist_id, listbox):
    print("Entry is - ", artist_id)
    tracks = spotG.getTracksOfArtist(artist_id)
    i = 1
    for track in tracks:
        listbox.insert(i, track)
        i += 1
