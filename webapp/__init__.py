import requests
from flask import Flask, render_template

from webapp.map import fetch_coordinates


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    @app.route("/")
    def index():
        coordinates = fetch_coordinates(
            app.config["YANDEX_MAPS_API_KEY"],
            "Москва, Хохловский пер., 7/9 строение 2",
        )
        print(coordinates)

        return render_template(
            "index.html",
            apikey=app.config["YANDEX_MAPS_API_KEY"],
            page_title="Event Area",
            longitude=coordinates[0],
            latitude=coordinates[1],
            use_zoom=17,
        )

    return app
