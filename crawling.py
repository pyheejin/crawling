import requests
import csv
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen


# csv file open
csv_filename_to_write = 'billboard_chart_100.csv'
csv_open = open(csv_filename_to_write, 'w', encoding='utf-8')
csv_writer = csv.writer(csv_open)
csv_writer.writerow(('rank','song','artist'))

# BeautifulSoup
url = 'https://www.billboard.com/charts/hot-100'
req = requests.get(url)
html = req.text
bs = BeautifulSoup(html, 'html.parser')

hot_list = bs.findAll('li', {'class':re.compile('chart-list__element')})
for hot in hot_list:
    # rank
    rank_class = hot.findAll('span',{'class': re.compile('chart-element__rank__number')})
    rank = rank_class[0].text
    rank = ' '.join(rank.split())

    # song
    song_class = hot.findAll('span',{'class': re.compile('chart-element__information__song')})
    song = song_class[0].text
    song = ' '.join(song.split())

    # artist
    artist_class = hot.findAll('span',{'class': re.compile('chart-element__information__artist')})
    artist = artist_class[0].text
    artist = ' '.join(artist.split())

    csv_writer.writerow((rank, song, artist))

csv_open.close()