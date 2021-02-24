import arrow
from datetime import timedelta
from dynaconf import settings
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from typing import Union, Optional, Any

from app.ext.db import get_db
from app.schema import authentication as authentication_schema, user as user_schema
from app.model import user as user_model
from app.service import user as user_service

oauth2_schema = OAuth2PasswordBearer(tokenUrl='/user/api/login')


def authenticate_user(db: Session, form: OAuth2PasswordRequestForm) -> Union[
    user_model.User, HTTPException]:
    user = user_service.get_user_by_email(db, form.username)
    if not user.check_password(form.password):
        raise HTTPException(status_code=404, detail='Wrong password')
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = arrow.get(arrow.now(settings.TIMEZONE) + expires_delta).datetime
    else:
        expire = arrow.now(settings.TIMEZONE).shift(minutes=+15).datetime
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(claims=to_encode, key=settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_schema)) -> Any:
    try:
        payload = jwt.decode(token=token, key=settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get('sub')
        if email is None:
            raise HTTPException(status_code=401, detail='Could not validade credentials',
                                headers={'WWW-Authenticate': 'Bearer'})
        token_data = authentication_schema.TokenData(access_token=token, email=email)
    except JWTError:
        raise HTTPException(status_code=401, detail='Could not validade credentials',
                            headers={'WWW-Authenticate': 'Bearer'})
    return user_service.get_user_by_email(db=db, email=token_data.email)


async def is_active(current_user: user_schema.UserIn = Depends(get_current_user)) \
        -> Union[user_schema.UserIn, HTTPException]:
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail='User is not active')
    return current_user
