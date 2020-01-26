from flask_restplus import fields
from app import app_api

UserLoginBody = app_api.model('UserLoginBody', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})

UserData = app_api.model('UserData', {
    'id': fields.Integer(required=True, description='User id'),
    'email': fields.String(required=True, description='User email'),
    'username': fields.String(required=True, description='User name'),
    'token': fields.String(required=True, description='User token'),
})
