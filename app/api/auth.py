from app import app_api
from flask_restplus import Resource
from flask import abort
from app.models.domain.user import User
from app.models.schemas.user import UserData, UserLoginBody
from app.utils.users import get_user_data

ns = app_api.namespace('Auth', path='/api/auth')


@ns.route('/login')
class LoginUser(Resource):

    @ns.expect(UserLoginBody)
    @ns.marshal_with(UserData, code=200)
    def post(self):
        '''Авторизация '''
        user = User.get_user_by_email(email=app_api.payload['email'])
        if (user is None or
                not user.check_password(app_api.payload['password'])):
            abort(403)

        return get_user_data(user)
