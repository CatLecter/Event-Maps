import json
import os

from map.utils import fetch_coordinates
from pymongo import MongoClient
from pymongo.collection import Collection


def mongo_connect() -> Collection:
    client = MongoClient(os.getenv('MONGO_LINK'))
    db = client['db']
    collection = db['events']
    return collection


def add_balloon_content(
    address,
    event_id,
    event_url,
    header,
    second_header,
    contacts,
    creator_login,
    avatar_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSezXuEt5Tsu-hGhmEmHrEq_cr2Ec_3ds1gdXOnsxoYZDJfV33AKn8c2kh1OW6_BLzuuFk&usqp=CAU',
    description='Описание отсутствует',
    tags=[],
):
    coordinate = fetch_coordinates(address)
    latitude = coordinate[1]
    longitude = coordinate[0]

    balloonContent = {
        'type': 'Feature',
        'id': event_id,
        'geometry': {'type': 'Point', 'coordinates': [latitude, longitude]},
        'properties': {
            'balloonContentHeader': f'<a href = "{event_url}">{header}</a><br><span class="description">{second_header}</span>',
            'balloonContentBody': f'<img src="{avatar_url}" width="200"><br/><a href="{contacts}">{contacts}</a><br/><b>{address}</b><br/>{description}',
            'balloonContentFooter': f'<a class="btn btn-warning" href="#" role="button">Принять участие</a>',
            'hintContent': f'{tags}',
        },
    }
    collection = mongo_connect()
    collection.insert_one(balloonContent)


def create_ballon_json(events):
    received_balloon = []

    for event in events:
        balloon_data = mongo_connect().find_one({'id': event.id})
        latitude = float(balloon_data['geometry']['coordinates'][0])
        longitude = float(balloon_data['geometry']['coordinates'][1])

        receiv_description = {
            'type': balloon_data['type'],
            'id': balloon_data['id'],
            'geometry': {
                'type': balloon_data['geometry']['type'],
                'coordinates': [latitude, longitude],
            },
            'properties': {
                'balloonContentHeader': balloon_data['properties']['balloonContentHeader'],
                'balloonContentBody': balloon_data['properties']['balloonContentBody'],
                'balloonContentFooter': balloon_data['properties']['balloonContentFooter'],
                'hintContent': balloon_data['properties']['hintContent'],
            },
        }
        received_balloon.append(receiv_description)

    balloons = {'type': 'FeatureCollection', 'features': received_balloon}
    balloons_json = json.dumps(balloons, sort_keys=True, indent=4)

    with open('data.json', 'w') as write_file:
        json.dump(balloons_json, write_file)
