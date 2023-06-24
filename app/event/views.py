from datetime import datetime

from db import db
from event.balloon_content import add_balloonContent
from event.forms import EventRegForm
from event.models import Event
from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user

blueprint = Blueprint('event', __name__, url_prefix='/event')


@blueprint.route('/reg')
def event_reg():
    if not current_user.is_authenticated:
        return redirect(url_for('user.login'))
    title = 'EVENTS'
    login_form = EventRegForm()
    return render_template(
        'event/registration.html',
        page_title=title,
        form=login_form,
    )


@blueprint.route('/process-event-reg', methods=['POST'])
def process_event_reg():
    form = EventRegForm()
    if form.validate_on_submit():
        start_date = datetime(
            year=int(form.start_year.data),
            month=int(form.start_month.data),
            day=int(form.start_day.data),
            hour=int(form.start_hour.data),
            minute=int(form.start_minutes.data),
        )
        end_date = datetime(
            year=int(form.end_year.data),
            month=int(form.end_month.data),
            day=int(form.end_day.data),
            hour=int(form.end_hour.data),
            minute=int(form.end_minutes.data),
        )
        new_event = Event(
            creator_id=current_user.id,
            creator_login=current_user.login,
            header=form.header.data,
            second_header=form.second_header.data,
            address=form.address.data,
            contacts=form.contacts.data,
            start_date=start_date,
            end_date=end_date,
            event_url=form.event_url.data,
            avatar_url=form.avatar_url.data,
        )
        db.session.add(new_event)
        db.session.commit()
        add_balloonContent(
            form.address.data,
            new_event.id,
            form.event_url.data,
            form.header.data,
            form.second_header.data,
            form.contacts.data,
            current_user.login,
            form.avatar_url.data,
            form.description.data,
        )
        flash('Событие успешно зарегистрировались!')
        return redirect(url_for('map.index'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'Ошибка в поле {getattr(form, field).label.text}: - {error}')
        return redirect(url_for('event.event_reg'))
