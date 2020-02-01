from app.utils.errors import EntityDoesNotExist
from app.models.domain.user import User


def check_email_is_taken(email: str) -> bool:
    try:
        user = User.query.filter_by(email=email).first()
        if user is None:
            return False
    except EntityDoesNotExist:
        return False

    return True
