from webapp import create_app

from webapp.event.models import Event


app = create_app()


with app.app_context():

    events = Event.query.filter_by(creator_login="vasi1988").all()
    for event in events:
        print(f"{event.start_date} - {event.header}")
