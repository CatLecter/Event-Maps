from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, TextAreaField
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
        render_kw={
            "class": "form-control fw-lighter",
            "placeholder": "Контакты организатора",
        },
    )

    event_url = StringField(
        "Ссылка на страницу (при наличии)",
        validators=[DataRequired()],
        render_kw={
            "class": "form-control fw-lighter",
            "placeholder": "Ссылка на страницу",
        },
    )

    avatar_url = StringField(
        "Аватар",
        validators=[DataRequired()],
        render_kw={
            "class": "form-control fw-lighter",
            "placeholder": "Ссылка на аватар",
        },
    )

    start_day = StringField(
        "Время и дата начала",
        validators=[DataRequired()],
        render_kw={"class": "form-control fw-lighter", "placeholder": "Число"},
    )

    start_month = StringField(
        "Время и дата начала",
        validators=[DataRequired()],
        render_kw={"class": "form-control fw-lighter", "placeholder": "Месяц"},
    )

    start_year = StringField(
        "Время и дата начала",
        validators=[DataRequired()],
        render_kw={"class": "form-control fw-lighter", "placeholder": "Год"},
    )

    start_hour = StringField(
        "Время и дата начала",
        validators=[DataRequired()],
        render_kw={"class": "form-control fw-lighter", "placeholder": "Часы"},
    )

    start_minutes = StringField(
        "Время и дата начала",
        validators=[DataRequired()],
        render_kw={"class": "form-control fw-lighter", "placeholder": "Минуты"},
    )

    end_day = StringField(
        "Время и дата окончания",
        validators=[DataRequired()],
        render_kw={"class": "form-control fw-lighter", "placeholder": "Число"},
    )

    end_month = StringField(
        "Время и дата окончания",
        validators=[DataRequired()],
        render_kw={"class": "form-control fw-lighter", "placeholder": "Месяц"},
    )

    end_year = StringField(
        "Время и дата окончания",
        validators=[DataRequired()],
        render_kw={"class": "form-control fw-lighter", "placeholder": "Год"},
    )

    end_hour = StringField(
        "Время и дата окончания",
        validators=[DataRequired()],
        render_kw={"class": "form-control fw-lighter", "placeholder": "Часы"},
    )

    end_minutes = StringField(
        "Время и дата окончания",
        validators=[DataRequired()],
        render_kw={"class": "form-control fw-lighter", "placeholder": "Минуты"},
    )

    description = TextAreaField(
        "Описание события",
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "id": "floatingTextarea",
            "style": "height: 100px",
        },
    )

    submit = SubmitField("Создать", render_kw={"class": "btn btn-primary fw-bolder"})
