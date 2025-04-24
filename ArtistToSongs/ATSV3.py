import requests
import unicodedata
from bs4 import BeautifulSoup
import time

IDs = []

with open("../artistAndIDs.txt", "r", encoding="utf-8") as file:
    for line in file:
        artist, artID = line.strip().split(": ", 1)
        IDs.append(artID)

startTime = int(time.time() * 1000)

with open("Big3(attempt 2 (FUCK TYLER, THE CREATOR)).txt", "w", encoding="utf-8") as file:
    file.write("Artist, SongTitle, SongSpotifyID\n")

i = 1

for ID in IDs:
    url = f"https://kworb.net/spotify/artist/{ID}_songs.html"
    print(f"{url} {i}")
    i += 1
    response = requests.get(url)
    response.encoding = 'utf-8'

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        artist = soup.find("span", class_="pagetitle")
        artistName = artist.text.strip().split("- ", 1)[0].strip()

        songList = []
        for tbody in soup.find_all('tbody'):
            for link in tbody.find_all('a'):
                id = link.get('href')[31:]
                title = unicodedata.normalize('NFC', link.text.strip())
                songList.append(f"{artistName}%:^ {title}%:^ {id}")

        with open("Big3(attempt 2 (FUCK TYLER, THE CREATOR)).txt", "a", encoding="utf-8") as file:
            for song in songList:
                file.write(song + "\n")

endTime = int(time.time() * 1000)
print("Total time (ms):", endTime - startTime)