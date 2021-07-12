from flask_login import current_user
from flask import Blueprint, redirect, render_template, url_for

from webapp.map.geocode import fetch_coordinates

blueprint = Blueprint("map", __name__)


@blueprint.route("/")
def index():
    if not current_user.is_authenticated:
        return redirect(url_for("user.login"))
    title = "Neighbros"
    coordinate = fetch_coordinates(current_user.address)
    return render_template(
        "map/ymaps.html",
        page_title=title,
        zoom=16,
        lat=coordinate[1],
        long=coordinate[0],
        events=url_for("static", filename='scripts/data.json'),
    )
