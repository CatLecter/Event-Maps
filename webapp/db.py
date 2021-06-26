from pymongo import MongoClient

import config

# Установка соединения с MongoDB
db_client = MongoClient(config.MONGODB_CONNECT)


def add_user(
    first_name,
    last_name,
    email,
    login,
    password,
    home_address="",
    work_address="",
    phone_number="",
    age="",
    tags=[],
):

    # Подключаемся к БД.
    # Если такой БД нет, то она будет создана
    current_db = db_client[config.MONGODB_DB_NAME]

    # Получаем коллекцию из БД.
    # Если такой коллекции нет, то она будет создана
    collection = current_db[config.MONGODB_DB_USERS_COLLECTION]

    # Проверяем значение first_name.
    if len(first_name) == 0:
        user_result = {
            "error_code": 1,
            "message": "Введите имя!",
        }
        return user_result

    # Проверяем значение last_name.
    if len(last_name) == 0:
        user_result = {
            "error_code": 2,
            "message": "Введите фамилию!",
        }
        return user_result

    # Проверяем значение E-mail
    if len(email) == 0:
        user_result = {
            "error_code": 3,
            "message": "Введите E-mail!",
        }
        return user_result

    # Проверяем правильность формата E-mail
    if email.count("@") == 1:
        if email.count(".") == 0:
            user_result = {
                "error_code": 4,
                "message": "E-mail введён неверно!",
            }
            return user_result

    if not len(email.split("@")) <= len(email.split(".")):
        user_result = {
            "error_code": 5,
            "message": "E-mail введён неверно!",
        }
        return user_result

    # Проверяем в БД совпадения по E-mail.
    # Если совпадений нет, то добавляем нового пользователя в базу.
    if collection.count_documents({"email": email}) == 1:
        user_result = {
            "error_code": 6,
            "message": "Пользователь с таким E-mail адресом уже существует!",
        }
        return user_result
    else:
        # Передаём в коллекцию данные
        # пользователя в формате "ключ": "значение"
        event_map = {
            "first_name": first_name,
            "last_name": last_name,
            "login": login,
            "password": password,
            "email": email,
            "home_address": home_address,
            "work_address": work_address,
            "phone_number": phone_number,
            "age": age,
            "tags": tags,
        }

        # Добавляем запись в коллекцию
        get_user_data = collection.insert_one(event_map)
        print(f"{first_name} {last_name} зарегистрирован.")

        # Получаем id нового пользователя
        user_result = get_user_data.inserted_id
        user_result = {
            "error_code": 0,
            "message": get_user_data.inserted_id,
        }

        return user_result

"""
def find_data_user(find_value, parameter="_id", key="_id"):
    current_db = db_client[config.MONGODB_DB_NAME]
    collection = current_db[config.MONGODB_DB_EVENTS_COLLECTION]
    result_find = collection.find_one({parameter: find_value})[key]
    return result_find
"""
"""
def add_event(
    event_name,
    event_type=[],
    event_address,
    event_geo,
    contact_phone_number,
    email,
    limit_part,
    date_time,
    time_interval,
    iterance,
    participants_id,
):

    current_db = db_client[config.MONGODB_DB_NAME]

    collection = current_db[config.MONGODB_DB_EVENTS_COLLECTION]

    event_map = {
        "event_name": event_name,
        "event_type": event_type,
        "event_address": event_address,
        "event_geo": event_geo,
        "contact_phone_number": contact_phone_number,
        "email": email,
        "limit_part": limit_part,
        "date_time": date_time,
        "time_interval": time_interval,
        "iterance": iterance,
        "participants_id": participants_id,
    }

    get_event_data = collection.insert_one(event_map)

    event_result = get_event_data.inserted_id
    return event_result
"""

# print(find_data_user("Safronov"))
result = add_user("Vasilii", "Safronov", "vas3454353543i@1988mail.ru")
print(result["error_code"])
print(result["message"])
