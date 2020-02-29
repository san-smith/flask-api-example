from app import app_api, db, app
from flask_restplus import Resource
from app.models.domain.user import User
from app.models.schemas.user import UserLoginBody, UserSignupBody, UserToken
from app.models.schemas.errors import BaseError
from email_validator import validate_email, EmailNotValidError
from app.utils.auth import check_email_is_taken
from app.utils import jwt
from flask_restplus import reqparse


ns = app_api.namespace('Auth', path='/api/auth')


@ns.route('/login')
class LoginUser(Resource):
    @ns.expect(UserLoginBody)
    @ns.response(400, 'Bad request', BaseError)
    @ns.marshal_with(UserToken, code=200)
    def post(self):
        '''Авторизация '''
        user: User = User.get_user_by_email(email=app_api.payload['email'])
        if user is None:
            ns.abort(400, status='User not found', statusCode='400')
        if not user.check_password(app_api.payload['password']):
            ns.abort(400, status='Wrong password', statusCode='400')

        if jwt.token_is_expired(user.token, app.config['SECRET_KEY']):
            token = jwt.create_access_token_for_user(
                user,
                app.config['SECRET_KEY'],
            )
            user.set_token(token)
            db.session.commit()

        return {'token': user.token}


@ns.route('/signup')
class SignupUser(Resource):
    @ns.expect(UserSignupBody)
    @ns.response(400, 'Bad request', BaseError)
    @ns.marshal_with(UserToken, code=201)
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

        token = jwt.create_access_token_for_user(
            user, app.config['SECRET_KEY'])
        user.set_token(token)

        db.session.add(user)
        db.session.commit()

        return {'token': token}, 201


@ns.route('/logut')
@ns.doc(params={'Auth': {
    'in': 'header',
    'description': 'An authorization token',
    'required': True,
}})
class LogoutUser(Resource):
    def post(self):
        '''Сброс токена авторизации'''
        parser = reqparse.RequestParser()
        parser.add_argument(
            'Auth',
            location='headers',
            required=True,
            type=str,
        )
        args = parser.parse_args()
        token = args['Auth']
        user: User = User.get_user_by_token(token=token)
        if user is None:
            ns.abort(401, status='Unauthorised', statusCode='401')

        token = jwt.create_access_token_for_user(
            user,
            app.config['SECRET_KEY'],
        )
        user.set_token(token)
        db.session.commit()

        return 200
