from datetime import datetime
from sqlalchemy.orm import relationship

from webapp.db import db


event_tags = db.Table(
    "event_tags",
    db.Model.metadata,
    db.Column("event_id", db.Integer, db.ForeignKey("event.id"), primary_key=True),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"), primary_key=True),
)


class Event(db.Model):
    __tablename__ = "event"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creator_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False,
        index=True,
    )
    creator_login = db.Column(
        db.String,
        db.ForeignKey("user.login"),
        nullable=False,
        index=True,
    )
    header = db.Column(db.String, nullable=False, index=True)
    second_header = db.Column(db.String)
    event_url = db.Column(db.String, default="#")
    description = db.Column(db.Text, default="Описание отсутствует")
    avatar_url = db.Column(db.String, default="https://cdn.pixabay.com/photo/2020/07/01/12/58/icon-5359553_1280.png")
    address = db.Column(db.String, nullable=False, index=True)
    contacs = db.Column(db.String)
    date_start = db.Column(db.DateTime)
    date_end = db.Column(db.DateTime)
    create_date = db.Column(db.DateTime, default=datetime.now, index=True)
    tag = db.relationship("Tag", secondary=event_tags, backref="event", lazy="dynamic")

    def __repr__(self):
        return f"<Event: {self.event_name} id={self.id}>"
