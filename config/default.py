import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
SQLALCHEMY_ECHO = False
JWT_TOKEN_PREFIX = 'Token'
SECRET_KEY = 'secret'
SQLALCHEMY_DATABASE_URI = os.environ.get(
    'DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
