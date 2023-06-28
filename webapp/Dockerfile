FROM python:3.11.4-bookworm as base

RUN apt update && \
    apt upgrade -y && \
    pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false

FROM base

EXPOSE 8000

WORKDIR /usr/src/webapp

COPY . .

RUN poetry install --no-dev

CMD gunicorn --worker-class gevent --workers 3 --bind 0.0.0.0:8000 --log-level warning wsgi:app
