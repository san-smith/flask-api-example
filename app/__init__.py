from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_restplus import Api
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_cors import CORS

app: Flask = Flask(__name__, instance_relative_config=True)
CORS(app)
app.wsgi_app = ProxyFix(app.wsgi_app)

# Load the default configuration
app.config.from_object('config.default')

# Load the configuration from the instance folder
app.config.from_pyfile('config.py', silent=True)

# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration
app.config.from_envvar('APP_CONFIG_FILE', silent=True)

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

from app.models.domain import user  # noqa: E402, F401
from app.api import users, auth, errors  # noqa: E402, F401
