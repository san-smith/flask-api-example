from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    token = db.Column(db.String(180))

    def __repr__(self) -> str:
        return '<User {} {} {}>'.format(
            self.email,
            self.first_name,
            self.last_name,
        )

    def set_password(self, password) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password) -> bool:
        return check_password_hash(self.password_hash, password)

    def get_user_by_email(email: str):
        return User.query.filter_by(email=email).first()

    def get_user_by_token(token: str):
        return User.query.filter_by(token=token).first()

    def set_token(self, token):
        self.token = token

    @login.user_loader
    def load_user(self, id):
        return User.query.get(int(id))
