FROM python:3.11.4-slim-bookworm

EXPOSE 8000

WORKDIR /usr/src/webapp

RUN apt update && \
    apt upgrade -y && \
    pip install --upgrade pip

COPY . .

RUN pip --no-cache-dir install  \
    email-validator==2.0.0.post2 \
    Flask==2.3.2 \
    Flask-Login==0.6.2 \
    Flask-SQLAlchemy==3.0.5 \
    Flask-WTF==1.1.1 \
    gunicorn==20.1.0 \
    psycopg2-binary==2.9.6 \
    pymongo==4.4.0 \
    python-dotenv==1.0.0 \
    requests==2.31.0

CMD gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app
