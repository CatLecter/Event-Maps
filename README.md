# Event Map

## Выполните следующие команды:

### 1) Для включения виртуального окружения выполните команду:

######   Linux: source env/bin/activate
######   Windows: env/Scripts/activate

### 2) Для запуска сервера выполнить:

##### $env:FLASK_APP="webapp"
##### $env:FLASK_ENV="development"
##### $env:FLASK_DEBUG=1
##### python -m flask run

#### или:

######   ./run.sh

### 3) Создание миграции:

##### $env:FLASK_APP="webapp"
##### flask db init

### 4) Резервирование файла базы:

##### move webapp.db webapp.db.old

### 5) Применение миграции:

##### $env:FLASK_APP="webapp"
##### flask db migrate -m "текст коммита"
### 6) Обозначить миграцию как выполненную:
##### flask db stamp <Revision ID>
