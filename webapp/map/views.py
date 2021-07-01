from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user


blueprint = Blueprint("map", __name__, url_prefix="/map")


@blueprint.route("/ymaps")
def map():
    title = "HOME"
    return render_template(
        "map/ymaps.html",
        page_title=title,
    )
