from datetime import timedelta
from dynaconf import settings
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List

from app.ext.db import get_db
from app.service import user as user_service, authentication as authentication_service
from app.schema import user as user_schema, authentication as authentication_schema

router = APIRouter(prefix='/user', tags=['User'])


@router.get('/', response_model=List[user_schema.UserOut], description='Get list of all users')
def get_all_users(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return user_service.get_all_users(db=db, skip=skip, limit=limit)


@router.get('/{userid}', response_model=user_schema.UserOut, description='Get user by ID')
def get_user_by_id(db: Session = Depends(get_db), userid: int = None):
    return user_service.get_user_by_id(db, userid)


@router.post('/', response_model=user_schema.UserOut, description='Create a new user')
def create_new_user(db: Session = Depends(get_db), user: user_schema.UserRegister = Depends()):
    return user_service.create_new_user(db, user)


@router.put('/{userid}', response_model=user_schema.UserOut, description='Update user')
def update_user(db: Session = Depends(get_db), userid: int = 0, user: user_schema.UserIn = Depends()):
    return user_service.update_user(db, userid, user)


@router.patch('/{userid}', response_model=user_schema.UserOut, description='Update user fields')
def patch_user(db: Session = Depends(get_db), userid: int = 0, user: user_schema.UserPatch = Depends()):
    return user_service.patch_user(db, userid, user)


@router.delete('/{userid}', description='Delete user', responses={200: {'detail': 'User deleted'}},
               dependencies=[Depends(authentication_service.oauth2_schema)])
def delete_user(db: Session = Depends(get_db), userid: int = 0):
    return user_service.delete_user(db, userid)


@router.post('/login')
def login(db: Session = Depends(get_db), form: authentication_schema.Login = Depends()):
    user = authentication_service.authenticate_user(db, form)
    if not user:
        raise HTTPException(status_code=404, detail='Incorrect email or password', headers={'Authorization': 'Bearer'})
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = authentication_service.create_access_token(data={'sub': user.email},
                                                              expires_delta=access_token_expires)
    return {'access_token': access_token, 'token_type': 'Bearer'}

@router.post('/api/login')
def login(db: Session = Depends(get_db), form: OAuth2PasswordRequestForm = Depends()):
    user = authentication_service.authenticate_user(db, form)
    if not user:
        raise HTTPException(status_code=404, detail='Incorrect email or passwoord', headers={'Authorization': 'Bearer'})
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = authentication_service.create_access_token(data={'sub': user.email},
                                                              expires_delta=access_token_expires)
    return {'access_token': access_token, 'token_type': 'Bearer'}
