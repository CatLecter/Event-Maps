FROM python:3.10.5-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
EXPOSE 5000

WORKDIR /usr/src/server

COPY ./requirements.txt .

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD gunicorn wsgi:app -b 0.0.0.0:5000 -w 3 --reload --log-level debug
#    --access-logfile=/var/jenkins_home/workspace/log/access_print.log \
#    --error-logfile=/var/jenkins_home/workspace/log/error_print.log
