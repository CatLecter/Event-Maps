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
    creator_id = db.Column(db.Integer, index=True)
    creator_login = db.Column(db.Integer, index=True)
    header = db.Column(db.String, nullable=False, index=True)
    second_header = db.Column(db.String)
    event_url = db.Column(db.String, default="#")
    description = db.Column(db.Text, default="Описание отсутствует")
    avatar_url = db.Column(
        db.String,
        default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSezXuEt5Tsu-hGhmEmHrEq_cr2Ec_3ds1gdXOnsxoYZDJfV33AKn8c2kh1OW6_BLzuuFk&usqp=CAU",
    )
    address = db.Column(db.String, nullable=False, index=True)
    contacs = db.Column(db.String)
    start_date = db.Column(db.String)
    end_date = db.Column(db.String)
    create_date = db.Column(db.DateTime, default=datetime.now())
    tag = db.relationship("Tag", secondary=event_tags, backref="event", lazy="dynamic")
    party = db.Column(db.String, default="К событию ещё никто не присоединился")

    def __repr__(self):
        return f"<Event id={self.id}>"
