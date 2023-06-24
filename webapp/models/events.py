from datetime import datetime

from db import db
from models.tags import Tag

event_tags = db.Table(
    'events_tags',
    db.Model.metadata,
    db.Column('event_uuid', db.Integer, db.ForeignKey('event.id'), primary_key=True),
    db.Column('tag_uuid', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
)


class Event(db.Model):
    __tablename__ = 'events'  # noqa

    uuid = db.Column(db.UUID(as_uuid=True), primary_key=True, autoincrement=True)
    creator_id = db.Column(db.Integer, index=True)
    creator_login = db.Column(db.String, index=True)
    header = db.Column(db.String, nullable=False, index=True)
    second_header = db.Column(db.String)
    event_url = db.Column(db.String, default='#')
    avatar_url = db.Column(
        db.String,
        default='https://encrypted-tbn0.gstatic.com/'
                'images?q=tbn:ANd9GcSezXuEt5Tsu-hGhmEmHrEq_cr2Ec_3ds1gdXOnsxoYZDJfV33AKn8c2kh1OW6_BLzuuFk&usqp=CAU',
    )
    address = db.Column(db.String, nullable=False, index=True)
    contacts = db.Column(db.String)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    create_date = db.Column(db.DateTime, default=datetime.now())
    tag = db.relationship(Tag, secondary=event_tags, backref='event', lazy='dynamic')
    party = db.Column(db.String, default='К событию ещё никто не присоединился')

    def __repr__(self):
        return f'<Event id={self.id}>'
