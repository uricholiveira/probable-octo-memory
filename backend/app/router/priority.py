from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.ext.db import get_db
from app.service import priority as service, authentication as authentication_service
from app.schema import priority as schema, authentication as authentication_schema

router = APIRouter(prefix='/priority', tags=['Priority'])


@router.get('/all', response_model=List[schema.PriorityOut], description='Get list of all priorities')
def get_all_priorities(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return service.get_all_priorities(db=db, skip=skip, limit=limit)


@router.get('/', response_model=schema.PriorityOut, description='Get priority by ID')
def get_priority_by_id(db: Session = Depends(get_db), priority_id: int = None):
    return service.get_priority_by_id(db, priority_id)


@router.post('/', response_model=schema.PriorityOut, description='Create a new priority')
def create_new_priority(db: Session = Depends(get_db), priority: schema.PriorityBase = Depends()):
    return service.create_new_priority(db, priority)


@router.put('/', response_model=schema.PriorityOut, description='Update priority')
def update_priority(db: Session = Depends(get_db), priority_id: int = 0, priority: schema.PriorityBase = Depends()):
    return service.update_priority(db, priority_id, priority)


@router.patch('/', response_model=schema.PriorityOut, description='Update priority fields')
def patch_priority(db: Session = Depends(get_db), priority_id: int = 0, priority: schema.PriorityPatch = Depends()):
    return service.patch_priority(db, priority_id, priority)


@router.delete('/', description='Delete priority', responses={200: {'detail': 'Priority deleted'}},
               dependencies=[Depends(authentication_service.oauth2_schema)])
def delete_priority(db: Session = Depends(get_db), priority_id: int = 0):
    return service.delete_priority(db, priority_id)