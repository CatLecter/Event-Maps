import requests  # type: ignore[import]
from webapp.config import YANDEX_MAPS_API_KEY


def fetch_coordinates(place):
    base_url = "https://geocode-maps.yandex.ru/1.x"
    params = {"geocode": place, "apikey": YANDEX_MAPS_API_KEY, "format": "json"}
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    found_places = response.json()["response"]["GeoObjectCollection"]["featureMember"]
    most_relevant = found_places[0]
    lon, lat = most_relevant["GeoObject"]["Point"]["pos"].split(" ")
    return lon, lat
