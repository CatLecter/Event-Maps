from gevent.monkey import patch_all

patch_all()

from psycogreen.gevent import patch_psycopg  # noqa

patch_psycopg()

from app import create_app  # noqa

app = create_app()
