from event.balloon_content import create_ballon_json
from event.models import Event
from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user
from map.utils import fetch_coordinates

blueprint = Blueprint('map', __name__)


@blueprint.route('/')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('user.login'))
    title = 'EVENTS'
    coordinate = fetch_coordinates(current_user.address)

    # тут нужно исправить запрос на выборку рекомендуемых событий (по тегам)
    created_events = Event.query.filter_by(creator_login=current_user.login).all()

    if not isinstance(created_events, list):
        created_events = [created_events]

    create_ballon_json(created_events)
    user_events = []
    for event in created_events:
        user_events.append(f'{event.start_date} - {event.header}')
    return render_template(
        'content/content.html',
        page_title=title,
        zoom=16,
        lat=coordinate[1],
        long=coordinate[0],
        data=url_for('static', filename='data.json'),
        my_events=user_events,
    )


@blueprint.route('/all_events')
def all_events():
    if not current_user.is_authenticated:
        return redirect(url_for('user.login'))
    title = 'EVENTS'
    coordinate = fetch_coordinates(current_user.address)

    # запрос всех событий из базы
    created_events = Event.query.order_by(Event.id).all()

    create_ballon_json(created_events)
    user_events = []
    for event in created_events:
        user_events.append(f'{event.start_date} - {event.header}')
    return render_template(
        'content/content.html',
        page_title=title,
        zoom=16,
        lat=coordinate[1],
        long=coordinate[0],
        data=url_for('static', filename='data.json'),
        my_events=user_events,
    )


@blueprint.route('/my_events')
def my_events():
    if not current_user.is_authenticated:
        return redirect(url_for('user.login'))
    title = 'EVENTS'
    coordinate = fetch_coordinates(current_user.address)

    # запрос созданных мной событий из базы
    created_events = Event.query.filter_by(creator_login=current_user.login).all()

    create_ballon_json(created_events)
    user_events = []
    for event in created_events:
        user_events.append(f'{event.start_date} - {event.header}')
    return render_template(
        'content/content.html',
        page_title=title,
        zoom=16,
        lat=coordinate[1],
        long=coordinate[0],
        data=url_for('static', filename='data.json'),
        my_events=user_events,
    )
