from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import Union, List

from app.model import user as model
from app.schema import user as schema


def get_all_users(db: Session, skip: int = 0, limit: int = 100) -> List[model.User]:
    return db.query(model.User).offset(skip).limit(limit).all()


def get_user_by_id(db: Session, user_id: int) -> Union[model.User, HTTPException]:
    user = db.query(model.User).filter(model.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return user


def get_user_by_username(db: Session, username: str) -> Union[model.User, HTTPException]:
    user = db.query(model.User).filter(model.User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return user


def get_user_by_email(db: Session, email: str) -> Union[model.User, HTTPException]:
    user = db.query(model.User).filter(model.User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return user


def create_new_user(db: Session, user: schema.UserRegister) -> Union[model.User, HTTPException]:
    new_user = db.query(model.User).filter(model.User.email == user.email).first()
    if new_user:
        raise HTTPException(status_code=401, detail='User already registered')
    new_user = model.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def update_user(db: Session, user_id: int, user: schema.UserIn) -> Union[model.User, HTTPException]:
    updated_user = get_user_by_id(db, user_id)
    for field in user.dict(exclude_none=True):
        setattr(updated_user, field, user.dict()[field])
    db.add(updated_user)
    db.commit()
    db.refresh(updated_user)
    return updated_user


def patch_user(db: Session, user_id: int, user: schema.UserPatch) -> Union[model.User, HTTPException]:
    updated_user = get_user_by_id(db, user_id)
    for field in user.dict(exclude_unset=True, exclude_none=True):
        setattr(updated_user, field, user.dict()[field])
    db.add(updated_user)
    db.commit()
    db.refresh(updated_user)
    return updated_user


def delete_user(db: Session, user_id: int) -> Union[JSONResponse, HTTPException]:
    user = get_user_by_id(db, user_id)
    db.delete(user)
    db.commit()
    return JSONResponse(status_code=200, content={'detail': 'User deleted'})
