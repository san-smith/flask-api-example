from datetime import datetime, timedelta
from typing import Dict

from jwt import encode, decode, PyJWTError
# from pydantic import ValidationError

from app.models.domain.user import User

JWT_SUBJECT = "access"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # one week


def create_jwt_token(
    *, jwt_content: Dict[str, str], secret_key: str, expires_delta: timedelta
) -> str:
    to_encode = jwt_content.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({'exp': expire, 'sub': JWT_SUBJECT})
    return encode(to_encode, secret_key, algorithm=ALGORITHM).decode()


def create_access_token_for_user(user: User, secret_key: str) -> str:
    return create_jwt_token(
        jwt_content={'email': user.email},
        secret_key=secret_key,
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )


def get_email_from_token(token: str, secret_key: str) -> str:
    try:
        return decode(token, secret_key, algorithms=[ALGORITHM])['email']
    except PyJWTError as decode_error:
        raise ValueError("unable to decode JWT token") from decode_error
    # except ValidationError as validation_error:
    #     raise ValueError("malformed payload in token") from validation_error
