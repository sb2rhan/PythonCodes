from spotifyGet import getTracksOfArtist


artists = ["3YQKmKGau1PzlVlkL1iodx", "711MCceyCBcFnzjGY4Q7Un",
           "246dkjvS1zLTtiykXe5h60", "1Xyo4u8uXC1ZmMpatF05PJ",
           "3TVXtAsR1Inumwj472S9r4"]

while True:
    print("Welcome to Spotify Tracks Getter!")
    print("[1] - to print top tracks of Twenty One Pilots")
    print("[2] - to print top tracks of AC/DC")
    print("[3] - to print top tracks of Post Malone")
    print("[4] - to print top tracks of The Weeknd")
    print("[5] - to print top tracks of Drake")
    print("[0] - to exit")

    choice = int(input(">> "))

    if (choice == 0):
        print("Leaving...")
        break
    elif (choice < 0 and choice > 5):
        print("Incorrect option")
    else:
        tracks = getTracksOfArtist(artists[choice - 1])
        for t in tracks:
            print(t)
