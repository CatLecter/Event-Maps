from flask import Flask, render_template

from webapp.forms import LoginForm
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
            page_title="Neighbors",
            longitude=coordinates[0],
            latitude=coordinates[1],
            use_zoom=17,
        )

    @app.route("/login")
    def login():
        title = "Neighbors - Авторизация"
        login_form = LoginForm()
        return render_template(
            "login.html",
            page_title="Neighbors - Авторизация",
            form=login_form,
        )

    return app
