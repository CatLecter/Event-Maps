from pymongo import MongoClient

from webapp.config import MONGO_LINK
from webapp.map.utils import fetch_coordinates


def mongo_connect():
    client = MongoClient(MONGO_LINK)
    mongo_db = client.description
    collection = mongo_db.description
    return collection


def add_balloonContent(
    address,
    event_id,
    event_url,
    header,
    second_header,
    contacts,
    creator_login,
    avatar_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSezXuEt5Tsu-hGhmEmHrEq_cr2Ec_3ds1gdXOnsxoYZDJfV33AKn8c2kh1OW6_BLzuuFk&usqp=CAU",
    description="Описание отсутствует",
    tags=[],
):

    coordinate = fetch_coordinates(address)
    latitude = coordinate[1]
    longitude = coordinate[0]

    balloonContent = {
        "type": "Feature",
        "id": event_id,
        "geometry": {"type": "Point", "coordinates": [latitude, longitude]},
        "properties": {
            "balloonContentHeader": f"<a href = \"{event_url}\">{header}</a><br><span class=\"description\">{second_header}</span>",
            "balloonContentBody": f"<img src=\"{avatar_url}\" width=\"200\"><br/><a href=\"{contacts}\">{contacts}</a><br/><b>{address}</b><br/>{description}",
            "balloonContentFooter": f"<a class=\"btn btn-warning\" href=\"#\" role=\"button\">Принять участие</a>",
            "hintContent": f"{tags}",
        },
    }
    mongo_connect().insert_one(balloonContent)
