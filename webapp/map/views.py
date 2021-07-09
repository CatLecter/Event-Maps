from flask_login import current_user
from flask import Blueprint, redirect, render_template, url_for

blueprint = Blueprint("map", __name__)


@blueprint.route("/")
def index():
    if not current_user.is_authenticated:
        return redirect(url_for("user.login"))
    title = "HOME"
    return render_template(
        "map/ymaps.html",
        page_title=title,
    )
