x = 0

with open("Big3.txt", "r", encoding="utf-8") as file:
    for line in file:
        if (x > 200):
            break
        x += 1
        artist, songTitle, songID = line.strip().split(", ", 1)