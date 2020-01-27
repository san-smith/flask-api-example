from app import app_api
from flask_restplus import Resource
from flask import abort
from app.models.domain.user import User
from app.models.schemas.user import UserData
from app.utils.users import get_user_data

ns = app_api.namespace('User', path='/api/users')


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
