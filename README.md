# Flask RESTful API Example

Пример разработки RESTful API с использованием flask и flask-plus.

Для создания виртуального окружения выполните:

    python3 -m venv venv

Чтобы активировать это окружение выполните:

    source venv/bin/activate

## Install

Для установки необходимых зависимостей выполните:

    pip install -r requirements.txt

## Run

Для быстрого зстарта с использованием `sqlite` создайте в корне проекта файл `instance/config.py` со следующим содержимым:

    import os

    basedir = os.path.abspath(os.path.dirname(__file__))

    DEBUG = True  # Turns on debugging features in Flask
    SQLALCHEMY_ECHO = True
    SECRET_KEY = 'secret'

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

В этой же директории после запуска приложения будет расположен файл базы данных (`app.db`)

----

Для выполнения в дебаг-режиме выполните:

    bash ./start.sh 

Документация к реализованному API доступна по адресу: [http://127.0.0.1:5000/docs/](http://127.0.0.1:5000/docs/)

----

Для запуска с использованием `gunicorn` выполните:

    gunicorn -b 0.0.0.0:8000 -w 4 app:app

В этом случае документация к API расположена по адресу: [http://0.0.0.0:8000/docs/](http://0.0.0.0:8000/docs/)

## Project structure

Проект имеет следующую структуру:

    ├── app               - пакет с flask приложением.
    │   ├── api           - логика обработки запросов.
    |   ├── models        - модели сущностей
    │   └── utils         - различные утилиты и хелперы.
    ├── config            - файлы конфигурации в различных средах.
    ├── migrations        - alembic-миграции
    ├── tests             - тесты
    ├── README.md         - этот файл
    ├── requirements.txt  - зависимости проекта
    ├── run.py            - 
    └── start.sh          - файл для быстрого запуска в дебаг-режиме.
