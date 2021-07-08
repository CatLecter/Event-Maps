import sys

from webapp import create_app
from webapp.db import db
from webapp.tag.models import Tag


app = create_app()


with app.app_context():
    tag_value = input("Введите тэг: ").replace(" ", "").strip("#").lower()
    tag = "#" + tag_value
    if Tag.query.filter(Tag.tag == tag).count():
        print("Такой тэг уже существует!")
        sys.exit(0)
    else:
        new_tag = Tag(tag=tag)
        db.session.add(new_tag)
        db.session.commit()

        print(f"Создан тэг с id={new_tag.id}")
