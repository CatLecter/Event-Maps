from datetime import datetime

from webapp.db import db


tags = db.Table(
    "event_tags",
    db.Model.metadata,
    db.Column("event_id", db.Integer, db.ForeignKey("event.id"), primary_key=True),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"), primary_key=True),
)


class Event(db.Model):
    __tablename__ = "event"

    """
    Список необходимых полей:
       + event_id,
       + event_url="#",
       + event_header,
       + second_header,
       + event_description,
       + avatar_url,
       + creator_login,
       + contact,
       + address
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creator_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    creator_login = db.Column(db.String, db.ForeignKey("user.login"), nullable=False)
    header = db.Column(db.String, nullable=False)
    second_header = db.Column(db.String)
    url = db.Column(db.String, default="#")
    description = db.Column(db.Text, default="Описание отсутствует")
    avatar = db.Column(db.String, default="/static/images/avatars/event/event.jpg")
    address = db.Column(db.String, nullable=False)
    contacs = db.Column(db.String)
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    # tag = db.relationship("Tag", backref="event", lazy="dynamic")
    path_to_avatar = db.Column(db.String)

    def __repr__(self):
        return f"<Event: {self.event_name} id={self.id}>"
