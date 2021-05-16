"""
Scrapes lyrics using BS4
========================
Select how many songs to scrape at a time
catch incorrect artist inputs
allow the user to input more than a sing
"""

import os
import re
import requests
from bs4 import BeautifulSoup as soup
from pyfiglet import Figlet

BASE_URL = 'http://www.lyrics.com'
HEADERS = {'headers': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36"}


def slugify(name):
    """return artist or song name to use in URLs and filenames"""
    return name.lower().strip().replace(' ', '-').replace('+', '_')


def read_artist_page(artist):
    """finds URLs for an artist name and returns a list"""
    url = BASE_URL + '/artist/' + artist
    print(f'reading artist page: {url}')
    artist_page = requests.get(url, headers=HEADERS)
    return artist_page.text


def extract_song_links(artist_page):
    """Returns a dict of {song name: song_url}"""
    songs = {}
    artist_bs4 = soup(artist_page, 'html.parser')
    regex = r'/lyric/\d+/[^/]+/(\S+)'
    for div in artist_bs4.find_all(attrs={'class':'tal qx'}):
        for link in div.find_all('a'):
            url = link.get('href')
            name = re.findall(regex, url)[0]
            songs[name] = BASE_URL + url

    print(f'\nfound {len(songs)} song URLs\n')
    return songs


def download_song(url, filename):
    """downloads a single song and saves it to a file"""
    page = requests.get(url, headers=HEADERS)
    if page.status_code == 200:  # OK
        with open(filename, 'w') as outf:
            outf.write(page.text)
    else:
        print(f'download failed with status code {page.status_code}!')


def scrape_songs(artist, songs):
    """
    downloads all songs from a {name: url} dictionary
    and saves them to HTML files
    """
    path = f'songs/{artist}'
    if not os.path.exists(path):
        os.makedirs(path)

    for song_name, url in songs.items():
        song_name = slugify(song_name)
        filename = f'{path}/{song_name}.html'
        if os.path.exists(filename):
            print(f'file {filename} exists, skipping')
        else:
            print(f'downloading song: {song_name} from {url}')
            download_song(url, filename)


def input_artists():
    """Collect artist names until user presses Enter"""
    artists = []
    name = "dummy"  # otherwise loop does not start
    while name:
        name = input("\nPlease enter names of artists to scrape. Press 'Enter' to finish:\n\n ")
        artists.append(name)

    return artists[:-1]  # last artist is empty


if __name__ == '__main__':
    # title
    print(Figlet().renderText('Lyrics Scraper\n'))

    # output directory
    if not os.path.exists('songs'):
        os.makedirs('songs')

    # main program
    for artist in input_artists():
        artist = slugify(artist)
        html = read_artist_page(artist)
        songs = extract_song_links(html)
        scrape_songs(artist, songs)
