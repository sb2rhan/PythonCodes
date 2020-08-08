import tkinter as tk
from Functions import getTracksOfArtist

# constants
WIDTH = 600
HEIGHT = 500
FONT = 10

root = tk.Tk()
root.title("Spotify Tracks Getter")

# for presenting every widget
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='#297c4e')
canvas.pack()

# frame for search bar and button
upper_frame = tk.Frame(canvas, bd=5)
upper_frame.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.09, anchor='n')

label = tk.Label(upper_frame, text="Enter id of artist: ", font=FONT)
label.place(relx=0, rely=0, relwidth=0.3, relheight=1)

entry_bar = tk.Entry(upper_frame, font=FONT)
entry_bar.place(relx=0.35, rely=0, relwidth=0.35, relheight=1)

button = tk.Button(upper_frame, text="Search tracks", fg="green",
                   font=FONT,
                   command=lambda:
                   getTracksOfArtist(entry_bar.get(), list_box))
button.place(relx=0.75, rely=0, relwidth=0.25, relheight=1)

# for presenting list of tracks
lower_frame = tk.Frame(canvas, bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.9, relheight=0.7, anchor='n')

scrollbar = tk.Scrollbar(lower_frame, orient="horizontal")
scrollbar.pack(side="bottom", fill="x")

# for storing tracks
list_box = tk.Listbox(lower_frame, width=150, height=50, xscrollcommand=scrollbar.set)
list_box.pack(fill="both")

scrollbar.config(command=list_box.xview)

root.mainloop()
