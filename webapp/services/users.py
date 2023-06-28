from datetime import datetime

from db.postgres import PostgresDB
from dependencies import container
from schemes.users import User


class UserService:
    def __init__(self):
        self.db: PostgresDB = container.resolve(PostgresDB)

    def get_user(self, user_uuid: str) -> dict | None:
        user = self.db.execute(
            'SELECT email, login, full_name, phone, photo, location, role, created_at, updated_at '
            'FROM users WHERE uuid = %s',
            (user_uuid,),
        )
        return user or None

    def add_user(self, user: User) -> dict | None:
        user_uuid = self.db.execute(
            'INSERT INTO users(email, password, login, full_name, phone, photo, location, role) '
            'VALUES(%s, %s, %s, %s, %s, %s, point(%s, %s), %s) RETURNING uuid',
            (
                user.email,
                user.password,
                user.login,
                user.full_name,
                user.phone,
                user.photo,
                user.latitude,
                user.longitude,
                user.role,
            ),
        )
        user = self.get_user(user_uuid['uuid'])
        return user

    def update_user(self, user_uuid: str, user: User) -> dict | None:
        uuid_updated_user = self.db.execute(
            'UPDATE users SET email = %s, password = %s, login = %s, full_name = %s, phone = %s, photo = %s, '
            'location = point(%s, %s), role = %s, updated_at = %s WHERE uuid = %s RETURNING uuid',
            (
                user.email,
                user.password,
                user.login,
                user.full_name,
                user.phone,
                user.photo,
                user.latitude,
                user.longitude,
                user.role,
                datetime.now(),
                user_uuid,
            ),
        )
        return self.get_user(uuid_updated_user['uuid']) if uuid_updated_user else None

    def delete_user(self, user_uuid: str) -> bool:
        uuid_deleted_user = self.db.execute('DELETE FROM users WHERE uuid = %s RETURNING uuid', (user_uuid,))
        return True if uuid_deleted_user else False

    def check_user_by_email(self, email: str) -> bool:
        user = self.db.execute('SELECT count(email) FROM users WHERE email = %s', (email,))
        return True if user['count'] > 0 else False

    def get_user_by_email(self, email: str) -> dict | None:
        user = self.db.execute(
            'SELECT uuid, email, login, full_name, phone, photo, location, role, created_at, updated_at '
            'FROM users WHERE email = %s',
            (email,),
        )
        return user or None


container.register(obj_type=UserService, instance=UserService())
