import sys

from webapp import create_app
from webapp.user.models import User


app = create_app()


with app.app_context():
    login = input("Введите Login для поиска: ")

    get_user_data = User.query.filter_by(login=login).first()

    user_tags = get_user_data.tags
    print(len(user_tags))
    for tag in user_tags:
        print(tag)
