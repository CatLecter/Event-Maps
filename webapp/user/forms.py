from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
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
