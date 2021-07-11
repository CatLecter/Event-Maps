<<<<<<< HEAD
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
=======
# import requests
from flask import Flask, render_template
>>>>>>> 7d84db149ccea6c7f3c7a20dbc14ce57cdf0c301


from webapp.db import db
from webapp.user.models import User
from webapp.event.models import Event
from webapp.tag.models import Tag
from webapp.admin.views import blueprint as admin_blueprint
from webapp.event.views import blueprint as event_blueprint
from webapp.user.views import blueprint as user_blueprint
from webapp.map.views import blueprint as map_blueprint
from webapp.news.views import blueprint as news_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "user.login"

    app.register_blueprint(admin_blueprint)
    app.register_blueprint(event_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(map_blueprint)
    app.register_blueprint(news_blueprint)

<<<<<<< HEAD
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
=======
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
>>>>>>> 7d84db149ccea6c7f3c7a20dbc14ce57cdf0c301

    return app
