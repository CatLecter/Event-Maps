from datetime import datetime

from flask_login import UserMixin
from geoalchemy2 import Geometry
from werkzeug.security import check_password_hash, generate_password_hash

from db import db
from models.events import Event
from models.tags import Tag

users_tags = db.Table(
    'users_tags',
    db.Model.metadata,
    db.Column('user_uuid', db.Integer, db.ForeignKey('users.uuid')),
    db.Column('tag_uuid', db.Integer, db.ForeignKey('tags.uuid')),
)


class User(db.Model, UserMixin):
    __tablename__ = 'users'  # noqa

    uuid = db.Column(db.UUID(as_uuid=True), primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String(128))
    login = db.Column(db.String(50), index=True, unique=True)
    full_name = db.Column(db.String)
    tag = db.relationship(Tag, secondary=users_tags, backref='users', lazy='dynamic')
    photo = db.Column(
        db.String,
        default='https://e7.pngegg.com/pngimages/207/508/'
                'png-clipart-computer-icons-youtube-avatar-user-avatar-mammal-face.png',
    )
    location = db.Column(Geometry('POINT'))
    role = db.Column(db.String(10), index=True, default='user')
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def get_my_events(self, login):
        my_events = Event.query.filter_by(creator_login=login).all()
        return my_events

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return f'<Login: {self.login} id={self.id}>'
