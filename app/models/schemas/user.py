from flask_restplus import fields
from app import app_api

UserLoginBody = app_api.model('UserLoginBody', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})

UserData = app_api.model('UserData', {
    'id': fields.Integer(required=True, description='User id'),
    'email': fields.String(required=True, description='User email'),
    'first_name': fields.String(required=True, description='User first name'),
    'last_name': fields.String(required=True, description='User last name'),
})


UserSignupBody = app_api.model('UserSignupBody', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password'),
    'first_name': fields.String(
        required=False,
        description='User first name, default ""',
    ),
    'last_name': fields.String(
        required=False,
        description='User last name, default ""',
    ),
})

UserToken = app_api.model('UserToken', {
    'token': fields.String(description='User token'),
})
