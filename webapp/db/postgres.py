import os
from typing import Any

from psycopg2 import DatabaseError, pool
from psycopg2.extras import RealDictCursor


class PostgresDB:
    def __init__(self):
        self.host = os.getenv('POSTGRES_HOST')
        self.port = os.getenv('POSTGRES_PORT')
        self.user = os.getenv('POSTGRES_USER')
        self.password = os.getenv('POSTGRES_PASSWORD')
        self.database = os.getenv('POSTGRES_DB')
        self.pool = None

    def _create_pool(self, min_size: int = 1, max_size: int = 20) -> None:
        if not self.pool:
            self.pool = pool.SimpleConnectionPool(
                cursor_factory=RealDictCursor,
                minconn=min_size,
                maxconn=max_size,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.database,
            )

    def execute(self, *args, **kwargs) -> Any:
        self._create_pool()
        conn = self.pool.getconn()
        try:
            with conn.cursor() as cursor:
                cursor.execute(*args, **kwargs)
                result = cursor.fetchone()
            conn.commit()
        except DatabaseError as exc:
            raise exc
        finally:
            self.pool.putconn(conn)
        return result or None

    def __call__(self, *args, **kwargs) -> None:
        self._create_pool()
