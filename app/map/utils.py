import os
from http import HTTPStatus

import requests


def fetch_coordinates(place):
    base_url = 'https://geocode-maps.yandex.ru/1.x'
    params = {
        'geocode': place,
        'apikey': os.getenv('YANDEX_MAPS_API_KEY'),
        'format': 'json',
    }
    response = requests.get(base_url, params=params)
    if response.status_code != HTTPStatus.OK:
        return 37.617698, 55.755864
    found_places = dict(response.json())
    found_places = found_places.get('response').get('GeoObjectCollection').get('featureMember')
    most_relevant = found_places[0]
    lon, lat = most_relevant.get('GeoObject').get('Point').get('pos').split(' ')
    return lon, lat
