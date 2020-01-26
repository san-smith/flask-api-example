from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_restplus import Api
from werkzeug.contrib.fixers import ProxyFix

app: Flask = Flask(__name__, instance_relative_config=True)
app.wsgi_app = ProxyFix(app.wsgi_app)

# Load the default configuration
app.config.from_object('config.default')

# Load the configuration from the instance folder
app.config.from_pyfile('config.py')

# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration
# app.config.from_envvar('APP_CONFIG_FILE')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

app_api = Api(
    app,
    version='1.0',
    title='Example API',
    description='A simple API',
    doc='/docs/',
)

from app.models.domains import user
from app.api import routes