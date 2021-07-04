from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user

from webapp.user.forms import LoginForm
from webapp.event.models import Event

blueprint = Blueprint("event", __name__, url_prefix="/event")


@blueprint.route("/event")
def login():
    if current_user.is_authenticated:
        return redirect(url_for("map.index"))
    title = "HOME"
    login_form = LoginForm()
    return render_template(
        "user/login.html",
        page_title=title,
        form=login_form,
    )
