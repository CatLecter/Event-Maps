from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


"""

class Event(db.Model):
    __tablename__ = "event"
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
    tag = db.relationship(
        "Tag",
        secondary=event_tags,
        backref="event",
        # lazy="dynamic"
    )
    path_to_avatar = db.Column(db.String)

    def __repr__(self):
        return f"<Event: {self.event_name} id={self.id}>"

"""


class EventRegForm(FlaskForm):
    login = StringField(
        "Login", validators=[DataRequired()],
        render_kw={"class": "form-control fw-lighter", "placeholder": "Login"}
    )
    email = StringField(
        "E-mail", validators=[DataRequired()],
        render_kw={"class": "form-control fw-lighter", "placeholder": "E-mail"}
    )
    password = PasswordField(
        "Password", validators=[DataRequired()],
        render_kw={"class": "form-control fw-lighter", "placeholder": "Password"}
    )
    remember_me = BooleanField("Запомнить меня", default=True, render_kw={"class": "form-check-input"})
    submit = SubmitField("Login", render_kw={"class": "btn btn-primary fw-bolder"})
