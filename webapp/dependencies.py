from db.postgres import PostgresDB
from rodi import Container

container = Container()

container.register(obj_type=PostgresDB, instance=PostgresDB())
