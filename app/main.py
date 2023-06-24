import os

from admin.views import blueprint as admin_blueprint
from db import db
from dotenv import find_dotenv, load_dotenv
from event.views import blueprint as event_blueprint
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from map.views import blueprint as map_blueprint
from news.views import blueprint as news_blueprint
from user.models import User
from user.views import blueprint as user_blueprint

load_dotenv(dotenv_path=find_dotenv(filename='.env'))


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['MONGO_LINK'] = os.getenv('MONGO_LINK')
    app.config['YANDEX_MAPS_API_KEY'] = os.getenv('YANDEX_MAPS_API_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    db.init_app(app)
    migrate = Migrate(app, db)  # noqa

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    app.register_blueprint(admin_blueprint)
    app.register_blueprint(event_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(map_blueprint)
    app.register_blueprint(news_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='127.0.0.1', port=8000, debug=True)
