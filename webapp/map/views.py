import json
import os
from flask_login import current_user
from flask import Blueprint, redirect, render_template, url_for
from pymongo import MongoClient

from webapp.config import MONGO_LINK
from webapp.map.utils import fetch_coordinates

from webapp.event.balloon_content import mongo_connect
from webapp.event.models import Event

blueprint = Blueprint("map", __name__)


@blueprint.route("/")
def index():
    if not current_user.is_authenticated:
        return redirect(url_for("user.login"))
    title = "Neighbros"
    coordinate = fetch_coordinates(current_user.address)

    created_events = Event.query.filter_by(creator_login=current_user.login).all()
    user_events = []
    received_balloon = []

    client = MongoClient(MONGO_LINK)
    mongo_db = client.description
    collection = mongo_db.description

    for event in created_events:
        user_events.append(f"{event.start_date} - {event.header}")
        balloon_data = collection.find_one({"id": event.id})
        latitude = float(balloon_data["geometry"]["coordinates"][0])
        longitude = float(balloon_data["geometry"]["coordinates"][1])
        receiv_description = {
            "type": balloon_data["type"],
            "id": balloon_data["id"],
            "geometry": {
                "type": balloon_data["geometry"]["type"],
                "coordinates": [latitude, longitude],
            },
            "properties": {
                "balloonContentHeader": balloon_data["properties"][
                    "balloonContentHeader"
                ],
                "balloonContentBody": balloon_data["properties"]["balloonContentBody"],
                "balloonContentFooter": balloon_data["properties"][
                    "balloonContentFooter"
                ],
                "hintContent": balloon_data["properties"]["hintContent"],
            },
        }
        received_balloon.append(receiv_description)
    balloons = {"type": "FeatureCollection", "features": received_balloon}
    balloons_json = json.dumps(balloons, sort_keys=True, indent=4)
    with open("data.json", "w") as write_file:
        json.dump(balloons_json, write_file)
    os.replace("data.json", "webapp/static/data.json")
    return render_template(
        "map/ymaps.html",
        page_title=title,
        zoom=16,
        lat=coordinate[1],
        long=coordinate[0],
        data=url_for("static", filename="data.json"),
        my_events=user_events,
    )
