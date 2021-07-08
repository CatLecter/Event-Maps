from webapp.event.models import Event


"""
Фрмат записи события:

{
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "id": 0,
            "geometry": {
                "type": "Point",
                "coordinates": [55.756006, 37.643264]
            },
            "properties": {
                "balloonContentHeader": "<a href = \"https://learn.python.ru/\">Learn Python</a><br><span class=\"description\">Курсы по программированию</span>",
                "balloonContentBody": "<img src=\"https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Python_logo_and_wordmark.svg/2560px-Python_logo_and_wordmark.svg.png\" height=\"150\" width=\"200\"><br/><a href=\"tel:+7 495 178-00-83\">+7 495 178-00-83</a><br/><b>Impact Hub (м. Китай-город)</b><br/>Защита проектов 17.07.21 г.",
                "balloonContentFooter": "Информация предоставлена:<br/>https://learn.python.ru/",
                "hintContent": "MoscowPython",
                "clusterCaption": "Learn Python"
            }
        }
    ]
}

"""


def get_data(
    event_id,
    latitude,
    longitude,
    event_url="#",
    event_header,
    second_header,
    event_description,
    avatar_url,
    creator_login,
    contact,
    address,
    teg_list
    ):

    event = {
        "type": "Feature",
        "id": event_id,
        "geometry": {"type": "Point", "coordinates": [latitude, longitude]},
        "properties": {
                "balloonContentHeader": f"<a href = \"{event_url}\">{event_header}</a><br><span class=\"description\">{second_header}</span>",
                "balloonContentBody": f"<img src=\"{avatar_url}\" width=\"200\"><br/><a href=\"{contact}\">{contact}</a><br/><b>{address}</b><br/>{event_description}",
                "balloonContentFooter": f"Организатор:<br/>{creator_login}",
                "hintContent": f"{teg_list}"
        }
    }

    data = {
        "type": "FeatureCollection",
        "features": [event]
    }
