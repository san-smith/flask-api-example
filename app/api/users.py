from app import app_api, db
from flask_restplus import Resource
from flask import jsonify, json, abort
from app.models.user import User

ns = app_api.namespace('User', path=f'/api/users')


@ns.route('/')
class Users(Resource):
    '''Взаимодействие с пользователями'''

    def get(self):
        '''Список пользователей'''
        users = User.query.all()
        return jsonify([user.serialize() for user in users])


@ns.route('/<int:id>')
@ns.response(404, 'User not found')
@ns.param('id', 'id пользователя')
class GetUser(Resource):
    @ns.doc('get_user')
    
    def get(self, id):
        '''Получить пользователя по id'''
        user = User.query.get(id)
        if user is None: return abort(404)
        return jsonify(user.serialize())
