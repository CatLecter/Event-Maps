import requests
from flask import Flask, render_template


from keys import YANDEX_MAPS_API_KEY


def fetch_coordinates(apikey, place):
    base_url = "https://geocode-maps.yandex.ru/1.x"
    params = {"geocode": place, "apikey": apikey, "format": "json"}
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    found_places = response.json()["response"]["GeoObjectCollection"]["featureMember"]
    most_relevant = found_places[0]
    lon, lat = most_relevant["GeoObject"]["Point"]["pos"].split(" ")
    return lon, lat


app = Flask(__name__)


@app.route("/")
def index():
    coordinates = fetch_coordinates(
        YANDEX_MAPS_API_KEY, "Москва, Волгоградский проспект, 145/8"
    )
    print(coordinates)

    return render_template(
        "index.html",
        apikey=YANDEX_MAPS_API_KEY,
        page_title="Event Area",
        longitude=coordinates[0],
        latitude=coordinates[1],
        use_zoom=16,
    )


if __name__ == "__main__":
    app.run(debug=True)
