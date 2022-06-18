from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from webapp.db import db
from webapp.event.models import Event


users_tags = db.Table(
    "user_tags",
    db.Model.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id")),
)


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(50), index=True, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String(128))
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    address = db.Column(db.String)
    tag = db.relationship(
        "Tag",
        secondary=users_tags,
        backref="user",
        lazy="dynamic"
    )
    path_to_avatar = db.Column(db.String)
    role = db.Column(db.String(10), index=True, default="user")

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def get_my_events(self, login):
        my_events = Event.query.filter_by(creator_login=login).all()
        return my_events

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == "admin"

    def __repr__(self):
        return f"<Login: {self.login} id={self.id}>"
