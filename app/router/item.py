from datetime import timedelta
from dynaconf import settings
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.ext.db import get_db
from app.model import item as model, task as task_model, user as user_model
from app.schema import item as schema, task as task_schema
from app.service import item as service, authentication as authentication_service

router = APIRouter(prefix='/item', tags=['Item'])


@router.get('/', response_model=List[schema.ItemOut], description='Get list of all tasks')
def get_all_items(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return service.get_all_items(db=db, skip=skip, limit=limit)


@router.get('/{itemid}', response_model=schema.ItemOut, description='Get item by ID')
def get_item_by_id(db: Session = Depends(get_db), itemid: int = None):
    return service.get_item_by_id(db, itemid)


@router.post('/', response_model=schema.ItemOut, description='Create a new item')
def create_new_item(db: Session = Depends(get_db), item: schema.ItemBase = Depends()):
    return service.create_new_item(db, item)


@router.put('/{itemid}', response_model=schema.ItemOut, description='Update item')
def update_item(db: Session = Depends(get_db), itemid: int = 0, item: schema.ItemBase = Depends()):
    return service.update_item(db, itemid, item)


@router.patch('/{itemid}', response_model=schema.ItemOut, description='Update item fields')
def patch_item(db: Session = Depends(get_db), itemid: int = 0, item: schema.ItemPatch = Depends()):
    return service.patch_item(db, itemid, item)


@router.delete('/{itemid}', description='Delete item', responses={200: {'detail': 'Item deleted'}},
               dependencies=[Depends(authentication_service.oauth2_schema)])
def delete_item(db: Session = Depends(get_db), itemid: int = 0,
                user: user_model.User = Depends(authentication_service.get_current_user)):
    return service.delete_item(db, itemid, user)
