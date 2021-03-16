from datetime import timedelta
from dynaconf import settings
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.ext.db import get_db
from app.service import task as task_service, authentication as authentication_service
from app.schema import task as task_schema, authentication as authentication_schema

router = APIRouter(prefix='/task', tags=['Task'])


@router.get('/', response_model=List[task_schema.TaskOut], description='Get list of all tasks')
def get_all_tasks(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return task_service.get_all_task(db=db, skip=skip, limit=limit)


@router.get('/{taskid}', response_model=task_schema.TaskOut, description='Get task by ID')
def get_task_by_id(db: Session = Depends(get_db), taskid: int = None):
    return task_service.get_task_by_id(db, taskid)


@router.post('/', response_model=task_schema.TaskOut, description='Create a new task')
def create_new_task(db: Session = Depends(get_db), task: task_schema.TaskBase = Depends()):
    return task_service.create_new_task(db, task)


@router.put('/{taskid}', response_model=task_schema.TaskOut, description='Update task')
def update_task(db: Session = Depends(get_db), taskid: int = 0, task: task_schema.TaskBase = Depends()):
    return task_service.update_task(db, taskid, task)


@router.patch('/{taskid}', response_model=task_schema.TaskOut, description='Update task fields')
def patch_task(db: Session = Depends(get_db), taskid: int = 0, task: task_schema.TaskBase = Depends()):
    return task_service.patch_task(db, taskid, task)


@router.delete('/{taskid}', description='Delete task', responses={200: {'detail': 'Task deleted'}},
               dependencies=[Depends(authentication_service.oauth2_schema)])
def delete_task(db: Session = Depends(get_db), taskid: int = 0):
    return task_service.delete_task(db, taskid)