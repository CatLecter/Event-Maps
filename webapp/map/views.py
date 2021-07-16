import json
import os

from flask_login import current_user
from flask import Blueprint, redirect, render_template, url_for
from pymongo import MongoClient

from webapp.config import MONGO_LINK
from webapp.map.utils import fetch_coordinates
from webapp.map.forms import ChoiceAllForm, ChoiceRecommendedForm, ChoiceCreatedForm
from webapp.event.models import Event
from webapp.event.balloon_content import create_ballon_json

blueprint = Blueprint("map", __name__)


@blueprint.route("/")
def index():
    if not current_user.is_authenticated:
        return redirect(url_for("user.login"))
    title = "EVENTS"
    coordinate = fetch_coordinates(current_user.address)

    created_events = Event.query.filter_by(creator_login=current_user.login).all()
    # created_events = Event.query.order_by(Event.id).all()

    # create_ballon_json(created_events)

    user_events = []
    for event in created_events:
        user_events.append(f"{event.start_date} - {event.header}")

    return render_template(
        "map/ymaps.html",
        page_title=title,
        zoom=16,
        lat=coordinate[1],
        long=coordinate[0],
        data=url_for("static", filename="data.json"),
        my_events=user_events,
    )


@blueprint.route("/process-choice-all", methods=["POST"])
def process_choice_all():
    form = ChoiceAllForm()
    if form.validate_on_submit():
        all_events = Event.query.order_by(Event.id).all()
        create_ballon_json(all_events)
    return redirect(url_for("map.index"))


@blueprint.route("/process-choice-recommended", methods=["POST"])
def process_choice_recommended():
    form = ChoiceRecommendedForm()
    if form.validate_on_submit():
        recommended_events = Event.query.filter_by(
            creator_login=current_user.login
        ).all()
        create_ballon_json(recommended_events)
    return redirect(url_for("map.index"))


@blueprint.route("/process-choice-created", methods=["POST"])
def process_choice_created():
    form = ChoiceCreatedForm()
    if form.validate_on_submit():
        created_events = Event.query.filter_by(creator_login=current_user.login).all()
        create_ballon_json(created_events)
    return redirect(url_for("map.index"))
