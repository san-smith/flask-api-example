from app import app_api
from flask_restplus import Resource
from app.models.domain.user import User
from app.models.schemas.user import UserData, UserLoginBody
from app.models.schemas.errors import BaseError
from app.utils.users import get_user_data

ns = app_api.namespace('Auth', path='/api/auth')


@ns.route('/login')
class LoginUser(Resource):
    @ns.expect(UserLoginBody)
    @ns.response(400, 'Bad request', BaseError)
    @ns.marshal_with(UserData, code=200)
    def post(self):
        '''Авторизация '''
        user = User.get_user_by_email(email=app_api.payload['email'])
        if user is None:
            ns.abort(400, status='User not found', statusCode='400')
        if not user.check_password(app_api.payload['password']):
            ns.abort(400, status='Wrong password', statusCode='400')

        return get_user_data(user)
