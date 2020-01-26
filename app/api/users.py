from app import app_api, app
from flask_restplus import Resource
from flask import abort
from app.models.domain.user import User
from app.models.schemas.user import UserData, UserLoginBody
from app.utils import jwt
from typing import Dict, Any

ns = app_api.namespace('User', path=f'/api/users')


def get_user_data(user: User) -> Dict[str, Any]:
    token = jwt.create_access_token_for_user(
        user, app.config['SECRET_KEY'])
    return {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'token': token,
    }


@ns.route('/')
class Users(Resource):
    '''Взаимодействие с пользователями'''
    @ns.marshal_with(UserData, as_list=True, code=200)
    def get(self):
        '''Список пользователей'''
        users = User.query.all()
        return [get_user_data(user) for user in users]


@ns.route('/<int:id>')
@ns.response(404, 'User not found')
@ns.param('id', 'id пользователя')
class GetUser(Resource):
    @ns.doc('get_user')
    @ns.marshal_with(UserData, code=200)
    def get(self, id: int):
        '''Получить пользователя по id'''
        user = User.query.get(id)
        if user is None:
            return abort(404)

        return get_user_data(user)


@ns.route('/login')
class LoginUser(Resource):

    @ns.expect(UserLoginBody)
    @ns.marshal_with(UserData, code=201)
    def post(self):
        '''Авторизация '''
        print(app_api.payload)
