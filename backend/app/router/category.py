from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.ext.db import get_db
from app.service import category as service, authentication as authentication_service
from app.schema import category as schema, authentication as authentication_schema

router = APIRouter(prefix='/category', tags=['Category'])


@router.get('/', response_model=List[schema.CategoryOut], description='Get list of all categories')
def get_all_categories(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return service.get_all_categories(db=db, skip=skip, limit=limit)


@router.get('/', response_model=schema.CategoryOut, description='Get category by ID')
def get_category_by_id(db: Session = Depends(get_db), categoryid: int = None):
    return service.get_category_by_id(db, categoryid)


@router.post('/', response_model=schema.CategoryOut, description='Create a new category')
def create_new_category(db: Session = Depends(get_db), category: schema.CategoryBase = Depends()):
    return service.create_new_category(db, category)


@router.put('/', response_model=schema.CategoryOut, description='Update category')
def update_category(db: Session = Depends(get_db), categoryid: int = 0, category: schema.CategoryBase = Depends()):
    return service.update_category(db, categoryid, category)


@router.patch('/', response_model=schema.CategoryOut, description='Update category fields')
def patch_category(db: Session = Depends(get_db), categoryid: int = 0, category: schema.CategoryBase = Depends()):
    return service.patch_category(db, categoryid, category)


@router.delete('/', description='Delete category', responses={200: {'detail': 'Category deleted'}},
               dependencies=[Depends(authentication_service.oauth2_schema)])
def delete_category(db: Session = Depends(get_db), categoryid: int = 0):
    return service.delete_category(db, categoryid)