from webapp import create_app
from webapp.db import db
from webapp.tag.models import Tag
from webapp.event.models import Event


app = create_app()


with app.app_context():
    event_id = input("Введите id события: ")
    tag_value = input("Введите тэг: ").replace(" ", "").strip("#").lower()
    add_tag = "#" + tag_value
    event = Event.query.filter_by(id=event_id).one()
    print(f"Событие {event.header}.")
    if Tag.query.filter(Tag.tag == add_tag).count():
        event.tag = add_tag
        db.session.add(event)
        db.session.commit()
        print("Существующий тэг добавлен к событию.")
    else:
        new_tag = Tag(tag=add_tag)
        db.session.add(new_tag)
        db.session.commit()
        event.tag = add_tag
        db.session.add(event)
        db.session.commit()
        print(f"Создан тэг с id={new_tag.id} и добавлен к событию.")
