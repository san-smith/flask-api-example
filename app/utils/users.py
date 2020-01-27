from app import app
from app.models.domain.user import User
from app.utils import jwt
from typing import Dict, Any


def get_user_data(user: User) -> Dict[str, Any]:
    token = jwt.create_access_token_for_user(
        user, app.config['SECRET_KEY'])
    return {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'token': token,
    }
