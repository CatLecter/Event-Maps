import os

from dotenv import find_dotenv, load_dotenv
from flask import Flask
from views.auth import blueprint as auth_blueprint
from views.home import blueprint as home_blueprint
from views.users import blueprint as user_blueprint

load_dotenv(dotenv_path=find_dotenv(filename='.env'))


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['MONGO_LINK'] = os.getenv('MONGO_LINK')
    app.config['YANDEX_MAPS_API_KEY'] = os.getenv('YANDEX_MAPS_API_KEY')

    app.register_blueprint(home_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(user_blueprint)

    return app
