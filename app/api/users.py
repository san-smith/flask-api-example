from app import app_api, db
from flask_restplus import Resource
from flask import jsonify, json
from app.models.user import User

ns = app_api.namespace('User', path=f'/api/users')


@ns.route('/')
class Users(Resource):
    '''Взаимодействие с пользователями'''

    def get(self):
        '''Список пользователей'''
        users = User.query.all()
        return jsonify([user.serialize() for user in users])
