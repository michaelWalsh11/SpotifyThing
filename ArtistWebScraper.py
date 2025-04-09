import requests
import unicodedata
from bs4 import BeautifulSoup

urls = ['https://kworb.net/spotify/listeners.html', 'https://kworb.net/spotify/listeners2.html',
        'https://kworb.net/spotify/listeners3.html', 'https://kworb.net/spotify/listeners4.html',
        'https://kworb.net/spotify/listeners5.html']

artList = []
for url in urls:
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    for tbody in soup.find_all('tbody'):
        for link in tbody.find_all('a'):
            id = link.get('href')
            id = id[7: id.__len__() - 11]
            name = unicodedata.normalize('NFC', link.text.strip())
            artList.append(f"{name}: {id}")

for element in artList:
    print(element)

with open("artistAndIDs.txt", "w", encoding="utf-8") as file:
    for element in artList:
        file.write(element + "\n")
