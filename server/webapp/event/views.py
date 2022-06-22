from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user
from webapp.db import db
from webapp.event.balloon_content import add_balloonContent
from webapp.event.forms import EventRegForm
from webapp.event.models import Event

blueprint = Blueprint("event", __name__, url_prefix="/event")


@blueprint.route("/reg")
def event_reg():
    if not current_user.is_authenticated:
        return redirect(url_for("user.login"))
    title = "EVENTS"
    login_form = EventRegForm()
    return render_template(
        "event/registration.html",
        page_title=title,
        form=login_form,
    )


@blueprint.route("/process-event-reg", methods=["POST"])
def process_event_reg():
    form = EventRegForm()
    if form.validate_on_submit():
        new_event = Event(
            creator_id=current_user.id,
            creator_login=current_user.login,
            header=form.header.data,
            second_header=form.second_header.data,
            address=form.address.data,
            contacts=form.contacts.data,
            start_date=f"{form.start_day.data}.{form.start_month.data}.\
                        {form.start_year.data} г. в {form.start_hour.data}:\
                        {form.start_minutes.data}",
            end_date=f"{form.end_day.data}.{form.end_month.data}.{form.end_year.data} \
                        г. в {form.end_hour.data}:{form.end_minutes.data}",
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
        flash("Событие успешно зарегистрировались!")
        return redirect(url_for("map.index"))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Ошибка в поле {getattr(form, field).label.text}: - {error}")
        return redirect(url_for("event.event_reg"))
