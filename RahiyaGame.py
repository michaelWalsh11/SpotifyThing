import random

artists = []

with open("artistAndIDs.txt", "r", encoding="utf-8") as file:
    for line in file:
        artist, artID = line.strip().split(": ", 1)
        artists.append(artist)

i = 0

while i < 1:
    i += 1
    rand = random.randint(0, artists.__len__())
    print(artists[rand])
