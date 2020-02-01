from app import app_api, db
from flask_restplus import Resource
from app.models.domain.user import User
from app.models.schemas.user import UserData, UserLoginBody, UserSignupBody
from app.models.schemas.errors import BaseError
from app.utils.users import get_user_data
from email_validator import validate_email, EmailNotValidError
from app.utils.auth import check_email_is_taken


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


@ns.route('/signup')
class SignupUser(Resource):
    @ns.expect(UserSignupBody)
    @ns.response(400, 'Bad request', BaseError)
    @ns.marshal_with(UserData, code=201)
    def post(self):
        '''Регистрация '''
        try:
            email = app_api.payload['email']
            password = app_api.payload['password']
            first_name = app_api.payload.get('first_name', '')
            last_name = app_api.payload.get('last_name', '')
            validate_email(email)  # validate and get info

        except EmailNotValidError:
            ns.abort(400, status='Email is not valid', statusCode='400')
        except KeyError as e:
            ns.abort(
                422,
                status=f'Key "{str(e.args[0])}" is ubsent',
                statusCode='422',
            )

        if check_email_is_taken(email):
            ns.abort(400, status='Email has been taken', statusCode='400')

        user = User(first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        return get_user_data(user), 201
