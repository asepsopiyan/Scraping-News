import requests
from bs4 import BeautifulSoup

url = 'https://www.detik.com/terpopuler'
params = {
    'tag_from': 'wp_cb_mostPopular_more'
    }


res = requests.get(url, params=params)
soup = BeautifulSoup(res.text, 'html.parser')

populer_area = soup.find('div', 'grid-row list-content')
titles = populer_area.find_all('h3', 'media__title')
images = populer_area.find_all('div', 'media__image')
for image in images:
    print(image.find('a').find('img')['title'])
