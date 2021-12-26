import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detik-populer')
def detik_populer():
    url = 'https://www.detik.com/terpopuler'
    params = {
        'tag_from': 'wp_cb_mostPopular_more'
    }

    res = requests.get(url, params=params)
    soup = BeautifulSoup(res.text, 'html.parser')

    populer_area = soup.find('div', 'grid-row list-content')
    titles = populer_area.find_all('h3', 'media__title')
    images = populer_area.find_all('div', 'media__image')

    return render_template('index.html', images=images)

if __name__=='__main__':
    app.run(debug=True)

