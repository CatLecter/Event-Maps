from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField(
        "E-mail",
        validators=[DataRequired()],
        render_kw={
            "class": "form-control fw-lighter",
            "placeholder": "name@example.com",
            },
    )
    password = PasswordField(
        "Пароль",
        validators=[DataRequired()],
        render_kw={
            "class": "form-control fw-lighter",
            "placeholder": "Password",
            },
    )
    submit = SubmitField(
        "Вход",
        render_kw={"class": "btn btn-primary fw-bolder"},
    )
