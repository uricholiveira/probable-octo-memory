from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.ext.db import get_db
from app.service import situation as service, authentication as authentication_service
from app.schema import situation as schema, authentication as authentication_schema

router = APIRouter(prefix='/situation', tags=['Situation'])


@router.get('/all', response_model=List[schema.SituationOut], description='Get list of all situations')
def get_all_situations(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return service.get_all_situations(db=db, skip=skip, limit=limit)


@router.get('/', response_model=schema.SituationOut, description='Get situation by ID')
def get_situation_by_id(db: Session = Depends(get_db), situation_id: int = None):
    return service.get_situation_by_id(db, situation_id)


@router.post('/', response_model=schema.SituationOut, description='Create a new situation')
def create_new_situation(db: Session = Depends(get_db), situation: schema.SituationBase = Depends()):
    return service.create_new_situation(db, situation)


@router.put('/', response_model=schema.SituationOut, description='Update situation')
def update_situation(db: Session = Depends(get_db), situation_id: int = 0, situation: schema.SituationBase = Depends()):
    return service.update_situation(db, situation_id, situation)


@router.patch('/', response_model=schema.SituationOut, description='Update situation fields')
def patch_situation(db: Session = Depends(get_db), situation_id: int = 0, situation: schema.SituationPatch = Depends()):
    return service.patch_situation(db, situation_id, situation)


@router.delete('/', description='Delete situation', responses={200: {'detail': 'Situation deleted'}},
               dependencies=[Depends(authentication_service.oauth2_schema)])
def delete_situation(db: Session = Depends(get_db), situation_id: int = 0):
    return service.delete_situation(db, situation_id)