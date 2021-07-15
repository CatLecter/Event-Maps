from pymongo import MongoClient
from webapp import create_app

from webapp.config import MONGO_LINK
# from webapp.event.models import Event


app = create_app()


with app.app_context():


    """
    events = Event.query.filter_by(creator_login="CatLecter").all()
    for event in events:
        add_balloonContent(
            event.address,
            event.id,
            event.event_url,
            event.header,
            event.second_header,
            event.contacts,
            event.creator_login,
            event.avatar_url,
            description="Описание отсутствует",
        )
    """

client = MongoClient(MONGO_LINK)
mongo_db = client.description
collection = mongo_db.description

search = collection.find_one({"id": 8})
print(search)
