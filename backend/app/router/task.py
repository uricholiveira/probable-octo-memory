from datetime import timedelta
from dynaconf import settings
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.ext.db import get_db
from app.service import task as task_service, authentication as authentication_service
from app.schema import task as task_schema, authentication as authentication_schema

router = APIRouter(prefix='/task', tags=['Task'])


@router.get('/all', response_model=List[task_schema.TaskOut], description='Get list of all tasks')
def get_all_tasks(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return task_service.get_all_task(db=db, skip=skip, limit=limit)


@router.get('/', response_model=task_schema.TaskOut, description='Get task by ID')
def get_task_by_id(db: Session = Depends(get_db), task_id: int = None):
    return task_service.get_task_by_id(db, task_id)


@router.post('/', response_model=task_schema.TaskOut, description='Create a new task')
def create_new_task(db: Session = Depends(get_db), task_id: int = 0):
    return task_service.create_new_task(db, task_id)


@router.post('/start', response_model=task_schema.TaskOut, description='Start an task')
def start_task(db: Session = Depends(get_db), task_id: int = 0):
    return task_service.start_task(db, task_id)


@router.post('/pause', response_model=task_schema.TaskOut, description='Pause an task')
def pause_task(db: Session = Depends(get_db), task_id: int = 0):
    return task_service.pause_task(db, task_id)


@router.post('/deliver', response_model=task_schema.TaskOut, description='Deliver an task')
def deliver_task(db: Session = Depends(get_db), task_id: int = 0):
    return task_service.deliver_task(db, task_id)


@router.put('/', response_model=task_schema.TaskOut, description='Update task')
def update_task(db: Session = Depends(get_db), task_id: int = 0, task: task_schema.TaskBase = Depends()):
    return task_service.update_task(db, task_id, task)


@router.patch('/', response_model=task_schema.TaskOut, description='Update task fields')
def patch_task(db: Session = Depends(get_db), task_id: int = 0, task: task_schema.TaskPatch = Depends()):
    return task_service.patch_task(db, task_id, task)


@router.delete('/', description='Delete task', responses={200: {'detail': 'Task deleted'}},
               dependencies=[])
def delete_task(db: Session = Depends(get_db), task_id: int = 0):
    return task_service.delete_task(db, task_id)