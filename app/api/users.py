from app import app_api, db
from flask_restplus import Resource
from flask import jsonify, json, abort
from app.models.domains.user import User
from flask_login import current_user, login_user
from app.models.schemas.user import UserData, UserLoginBody

ns = app_api.namespace('User', path=f'/api/users')


@ns.route('/')
class Users(Resource):
    '''Взаимодействие с пользователями'''
    @ns.marshal_with(UserData, as_list=True, code=200)
    def get(self):
        '''Список пользователей'''
        users = User.query.all()
        return [user.serialize() for user in users]


@ns.route('/<int:id>')
@ns.response(404, 'User not found')
@ns.param('id', 'id пользователя')
class GetUser(Resource):
    @ns.doc('get_user')
    @ns.marshal_with(UserData, code=200)
    def get(self, id: int):
        '''Получить пользователя по id'''
        user = User.query.get(id)
        if user is None: return abort(404)
        return user.serialize()

@ns.route('/login')
class LoginUser(Resource):

    @ns.expect(UserLoginBody)
    @ns.marshal_with(UserData, code=201)
    def post(self):
        '''Авторизация '''
        print(app_api.payload)
        

