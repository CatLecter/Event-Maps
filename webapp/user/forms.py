from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    email = StringField(
        "E-mail",
        validators=[DataRequired()],
        render_kw={"class": "form-control fw-lighter", "placeholder": "E-mail"},
    )

    password = PasswordField(
        "Пароль",
        validators=[DataRequired()],
        render_kw={"class": "form-control fw-lighter", "placeholder": "Пароль"},
    )

    remember_me = BooleanField(
        "Запомнить меня", default=True, render_kw={"class": "form-check-input"}
    )
    submit = SubmitField("Войти", render_kw={"class": "btn btn-primary fw-bolder"})


class RegistrationForm(FlaskForm):
    first_name = StringField(
        "Имя",
        validators=[DataRequired()],
        render_kw={"class": "form-control fw-lighter", "placeholder": "Имя"},
    )

    last_name = StringField(
        "Фамилия",
        validators=[DataRequired()],
        render_kw={"class": "form-control fw-lighter", "placeholder": "Фамилия"},
    )

    login = StringField(
        "Логин",
        validators=[DataRequired()],
        render_kw={"class": "form-control fw-lighter", "placeholder": "Логин"},
    )

    email = StringField(
        "E-mail",
        validators=[DataRequired(), Email()],
        render_kw={"class": "form-control fw-lighter", "placeholder": "E-mail"},
    )

    address = StringField(
        "Адрес",
        validators=[DataRequired()],
        render_kw={"class": "form-control fw-lighter", "placeholder": "Адрес"},
    )

    password = PasswordField(
        "Пароль",
        validators=[DataRequired()],
        render_kw={"class": "form-control fw-lighter", "placeholder": "Пароль"},
    )

    repeat_password = PasswordField(
        "Повторите пароль",
        validators=[DataRequired(), EqualTo("password")],
        render_kw={
            "class": "form-control fw-lighter",
            "placeholder": "Повторите пароль",
        },
    )

    submit = SubmitField("Зарегистрироваться", render_kw={"class": "btn btn-primary fw-bolder"})
