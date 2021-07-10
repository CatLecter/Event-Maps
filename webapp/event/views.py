from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user

from webapp.db import db
from webapp.event.forms import EventRegForm
from webapp.event.models import Event

blueprint = Blueprint("event", __name__, url_prefix="/event")


@blueprint.route("/reg")
def event_reg():
    if not current_user.is_authenticated:
        return redirect(url_for("user.login"))
    title = "Neighbros"
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
            header=form.header.data,
            second_header=form.second_header.data,
            address=form.address.data,
            contacs=form.contacs.data,
            event_url=form.event_url.data,
            description=form.description.data,
            avatar_url=form.avatar_url.data,
        )
        db.session.add(new_event)
        db.session.commit()
        flash("Событие успешно зарегистрировались!")
        return redirect(url_for("map.index"))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Ошибка в поле {getattr(form, field).label.text}: - {error}")
        return redirect(url_for("event.event_reg"))
