from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class EventRegForm(FlaskForm):
    header = StringField(
        "Заголовок",
        validators=[DataRequired()],
        render_kw={"class": "form-control fw-lighter", "placeholder": "Заголовок"},
    )

    second_header = StringField(
        "Подзаголовок",
        validators=[DataRequired()],
        render_kw={"class": "form-control fw-lighter", "placeholder": "Подзаголовок"},
    )

    address = StringField(
        "Адрес",
        validators=[DataRequired()],
        render_kw={"class": "form-control fw-lighter", "placeholder": "Адрес"},
    )

    contacs = StringField(
        "Контактные данные организатора",
        validators=[DataRequired()],
        render_kw={"class": "form-control fw-lighter", "placeholder": "Контакты организатора"},
    )

    event_url = StringField(
        "Ссылка на страницу (при наличии)",
        validators=[DataRequired()],
        render_kw={"class": "form-control fw-lighter", "placeholder": "Ссылка на страницу"},
    )

    avatar_url = StringField(
        "Аватар",
        validators=[DataRequired()],
        render_kw={"class": "form-control fw-lighter",  "type": "file"},
    )
    
    description = TextAreaField(
        "Описание события",
        validators=[DataRequired()],
        render_kw={"class": "form-control", "id": "floatingTextarea", "style": "height: 150px"},
    )

    submit = SubmitField("Создать", render_kw={"class": "btn btn-primary fw-bolder"})
