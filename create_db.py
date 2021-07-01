from webapp import create_app
from webapp.model import db

db.create_all(app=create_app())
