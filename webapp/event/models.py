from datetime import datetime

from webapp.db import db


tags = db.Table(
    "event_tag",
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"), primary_key=True),
    db.Column("event_id", db.Integer, db.ForeignKey("event.id"), primary_key=True),
)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creator_id = db.Column(db.Integer, index=True)
    event_name = db.Column(db.String)
    address = db.Column(db.String)
    contacts = db.Column(db.String)
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    tags = db.relationship("Tag", backref="event", lazy="dynamic")
    path_to_avatar = db.Column(db.String)

    def __repr__(self):
        return f"<Event: {self.event_name} id={self.id}>"
