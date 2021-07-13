import webapp
from flask_login import current_user
from flask import Blueprint, redirect, render_template, url_for

from webapp.map.utils import fetch_coordinates
from webapp.event.models import Event

blueprint = Blueprint("map", __name__)


@blueprint.route("/")
def index():
    if not current_user.is_authenticated:
        return redirect(url_for("user.login"))
    title = "Neighbros"
    coordinate = fetch_coordinates(current_user.address)
    created_user_events = Event.query.filter_by(creator_login=current_user.login).all()
    user_events = []
    for event in created_user_events:
        user_events.append(f"{event.start_date} - {event.header}")
    return render_template(
        "map/ymaps.html",
        page_title=title,
        zoom=16,
        lat=coordinate[1],
        long=coordinate[0],
        events=url_for("static", filename="scripts/data.json"),
        my_events=user_events,
    )
