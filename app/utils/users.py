from app.models.domain.user import User
from typing import Dict, Any


def get_user_data(user: User) -> Dict[str, Any]:
    return {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
    }
