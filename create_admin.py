from getpass import getpass
import sys

from webapp import create_app
from webapp.db import db
from webapp.user.models import User


app = create_app()


with app.app_context():
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    login = input("Введите Login: ")
    if User.query.filter(User.login == login).count():
        print("Пользователь с таким Login уже существует")
        sys.exit(0)
    email = input("Введите E-mail: ")
    # tags = input("Введите тэг: ")
    if User.query.filter(User.email == email).count():
        print("Пользователь с таким E-mail уже существует")
        sys.exit(0)
    password = getpass("Введите пароль: ")
    password_repeat = getpass("Повторите пароль: ")
    if not password == password_repeat:
        print("Пароли не совпадают")
        sys.exit(0)

    new_admin = User(
        login=login,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
        # tags=tags,
        # role="admin",
    )

    new_admin.set_password(password)

    db.session.add(new_admin)
    db.session.commit()

    print(f"Создан пользователь с id={new_admin.id}")
