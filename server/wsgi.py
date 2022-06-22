from gevent import monkey

monkey.patch_all()

from webapp import create_app  # noqa: ignore[import]

app = create_app()
