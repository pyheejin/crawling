from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import re
import requests

# csv file open
csv_filename_to_write = 'billboard_chart_100_selector.csv'
csv_open = open(csv_filename_to_write, 'w', encoding='utf-8')
csv_writer = csv.writer(csv_open)
csv_writer.writerow(('rank','song','artist'))

# BeautifulSoup
url = 'https://www.billboard.com/charts/hot-100'
req = requests.get(url)
html = req.text
bs = BeautifulSoup(html, 'html.parser')

rank = bs.select("#charts > div > div.chart-list.container > ol > li > button > span.chart-element__rank.flex--column.flex--xy-center.flex--no-shrink > span.chart-element__rank__number")
song = bs.select("#charts > div > div.chart-list.container > ol > li > button > span.chart-element__information > span.chart-element__information__song.text--truncate.color--primary")
artist = bs.select("#charts > div > div.chart-list.container > ol > li > button > span.chart-element__information > span.chart-element__information__artist.text--truncate.color--secondary")

for hot in zip(rank, song, artist):
    rank = hot[0].text
    song = hot[1].text
    artist = hot[2].text

    csv_writer.writerow((rank, song, artist))

csv_open.close()