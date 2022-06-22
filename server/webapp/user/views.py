from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_user, logout_user
from webapp.db import db
from webapp.user.forms import LoginForm, RegistrationForm
from webapp.user.models import User

blueprint = Blueprint("user", __name__, url_prefix="/users")


@blueprint.route("/login")
def login():
    if current_user.is_authenticated:
        return redirect(url_for("map.index"))
    title = "EVENTS"
    login_form = LoginForm()
    return render_template(
        "user/login.html",
        page_title=title,
        form=login_form,
    )


@blueprint.route("/process-login", methods=["POST"])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash("Вы успешно вошли на сайт")
            return redirect(url_for("map.index"))
        else:
            flash("Вы неверно ввели пароль")
            return redirect(url_for("user.login"))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Ошибка в поле {getattr(form, field).label.text}: - {error}")
        return redirect(url_for("user.login"))


@blueprint.route("/logout")
def logout():
    logout_user()
    flash("Вы вышли")
    return redirect(url_for("user.login"))


@blueprint.route("/reg")
def reg():
    if current_user.is_authenticated:
        return redirect(url_for("map.index"))
    title = "EVENTS"
    login_form = RegistrationForm()
    return render_template(
        "user/registration.html",
        page_title=title,
        form=login_form,
    )


@blueprint.route("/process-reg", methods=["POST"])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            login=form.login.data,
            email=form.email.data,
            address=form.address.data,
            role="user",
        )
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash("Вы успешно зарегистрировались!")
        return redirect(url_for("user.login"))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Ошибка в поле {getattr(form, field).label.text}: - {error}")
        return redirect(url_for("user.process_reg"))
