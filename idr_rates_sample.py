import requests

# json_data = requests.get('http://www.floatrates.com/daily/idr.json')
json_data = {"usd":{"code":"USD","alphaCode":"USD","numericCode":"840","name":"U.S. Dollar","rate":7.032083126861e-5,"date":"Sun, 26 Dec 2021 23:55:01 GMT","inverseRate":14220.537242801},
             "eur":{"code":"EUR","alphaCode":"EUR","numericCode":"978","name":"Euro","rate":6.208898050934e-5,"date":"Sun, 26 Dec 2021 23:55:01 GMT","inverseRate":16105.917536358}}

for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])