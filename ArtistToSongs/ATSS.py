import requests
import unicodedata
from bs4 import BeautifulSoup
import time

IDs = []
songList = []

with open("../artistAndIDs.txt", "r", encoding="utf-8") as file:
    for line in file:
        artist, artID = line.strip().split(": ", 1)
        IDs.append(artID)

startTime = int(time.time() * 1000)

i = 1

for ID in IDs:
    url = f"https://kworb.net/spotify/artist/{ID}_songs.html"
    print(f"{url} {i}")
    i += 1
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        artist = soup.find("span", class_="pagetitle")
        artistName = artist.text.strip().split("- ", 1)[0].strip()

        for tbody in soup.find_all('tbody'):
            for link in tbody.find_all('a'):
                id = link.get('href')
                id = id[31 : ]
                title = unicodedata.normalize('NFC', link.text.strip())
                songList.append(f"{artistName}, {title}, {id}")


i = 0
x = 0
while x < songList.__len__():
    if x % 15000 is not 0:
        with open(f"Big3{i}.txt", "w", encoding="utf-8") as file:
            file.write("Artist, SongTitle, SongSpotifyID \n")
            for song in songList:
                file.write(song + "\n")

endTime = int(time.time() * 1000)

print(endTime - startTime)
