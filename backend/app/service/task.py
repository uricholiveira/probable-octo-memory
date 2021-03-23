from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import Union, List

from app.model import task as model
from app.schema import task as schema
from app.service import user as user_service, category as category_service, priority as priority_service, \
    situation as situation_service


def check_fields(db: Session, task: Union[schema.TaskBase, schema.TaskPatch]):
    user_service.get_user_by_id(db, task.dict().get('user_owner_id'))
    situation_service.get_situation_by_id(db, task.dict().get('situation_id'))
    priority_service.get_priority_by_id(db, task.dict().get('priority_id'))
    category_service.get_category_by_id(db, task.dict().get('category_id'))


def check_fields_to_create(db: Session, task: Union[schema.TaskBase, schema.TaskPatch]):
    user_service.get_user_by_id(db, task.dict().get('user_owner_id'))
    situation_service.get_situation_by_id(db, task.dict().get('situation_id'))


def get_all_task(db: Session, skip: int = 0, limit: int = 100) -> List[model.Task]:
    return db.query(model.Task).offset(skip).limit(limit).all()


def get_task_by_id(db: Session, task_id: int) -> Union[model.Task, HTTPException]:
    task = db.query(model.Task).filter(model.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail='Task not found')
    return task


def create_new_task(db: Session, task: schema.TaskCreate) -> Union[model.Task, HTTPException]:
    check_fields_to_create(db, task)
    category = category_service.get_category_by_id(db, task.dict().get('category_id'))
    new_task = model.Task(**task.dict(), priority_id=category.priority_id)

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    new_task_user = model.TaskUser(user=new_task.user_owner_id, task=new_task.id)
    db.add(new_task_user)
    db.commit()
    db.refresh(new_task)

    return new_task


def start_task(db: Session, task_id: int) -> Union[model.Task, HTTPException]:
    task = get_task_by_id(db, task_id)
    task.situation_id = 2

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


def pause_task(db: Session, task_id: int) -> Union[model.Task, HTTPException]:
    task = get_task_by_id(db, task_id)
    task.situation_id = 1

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


def deliver_task(db: Session, task_id: int) -> Union[model.Task, HTTPException]:
    task = get_task_by_id(db, task_id)
    task.situation_id = 5

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


def update_task(db: Session, task_id: int, task: schema.TaskBase) -> Union[model.Task, HTTPException]:
    check_fields(db, task)
    updated_task = get_task_by_id(db, task_id)
    for field in task.dict(exclude_none=True):
        setattr(updated_task, field, task.dict()[field])
    db.add(updated_task)
    db.commit()
    db.refresh(updated_task)
    return updated_task


def patch_task(db: Session, task_id: int, task: schema.TaskPatch) -> Union[model.Task, HTTPException]:
    check_fields(db, task)
    updated_task = get_task_by_id(db, task_id)
    for field in task.dict(exclude_unset=True, exclude_none=True):
        setattr(updated_task, field, task.dict()[field])
    db.add(updated_task)
    db.commit()
    db.refresh(updated_task)
    return updated_task


def delete_task(db: Session, task_id: int) -> Union[JSONResponse, HTTPException]:
    task = get_task_by_id(db, task_id)
    db.delete(task)
    db.commit()
    return JSONResponse(status_code=200, content={'detail': 'Task deleted'})
