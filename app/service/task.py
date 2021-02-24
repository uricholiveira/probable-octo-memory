from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import Union, List

from app.model import task as model
from app.schema import task as schema
from app.service import user as user_service


def get_all_task(db: Session, skip: int = 0, limit: int = 100) -> List[model.Task]:
    return db.query(model.Task).offset(skip).limit(limit).all()


def get_task_by_id(db: Session, taskid: int) -> Union[model.Task, HTTPException]:
    task = db.query(model.Task).filter(model.Task.id == taskid).first()
    if not task:
        raise HTTPException(status_code=404, detail='Taks not found')
    return task


def create_new_task(db: Session, task: schema.TaskBase) -> Union[model.Task, HTTPException]:
    is_user = user_service.get_user_by_id(db, task.dict().get('owner'))
    if not is_user:
        raise HTTPException(status_code=404, detail='User not found')
    new_task = model.Task(**task.dict())

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    new_task_user = model.TaskUser(user=new_task.owner, task=new_task.id, is_owner=True)
    db.add(new_task_user)
    db.commit()
    db.refresh(new_task)

    return new_task


def update_task(db: Session, taskid: int, task: schema.TaskBase) -> Union[model.Task, HTTPException]:
    updated_task = get_task_by_id(db, taskid)
    for field in task.dict(exclude_none=True):
        setattr(updated_task, field, task.dict()[field])
    db.add(updated_task)
    db.commit()
    db.refresh(updated_task)
    return updated_task


def patch_task(db: Session, taskid: int, task: schema.TaskBase) -> Union[model.Task, HTTPException]:
    updated_task = get_task_by_id(db, taskid)
    for field in task.dict(exclude_unset=True, exclude_none=True):
        setattr(updated_task, field, task.dict()[field])
    db.add(updated_task)
    db.commit()
    db.refresh(updated_task)
    return updated_task


def delete_task(db: Session, taskid: int) -> Union[JSONResponse, HTTPException]:
    task = get_task_by_id(db, taskid)
    db.delete(task)
    db.commit()
    return JSONResponse(status_code=200, content={'detail': 'Task deleted'})


def add_user_to_task(db: Session, task=schema.TaskUserBase) -> Union[model.Task, HTTPException]:
    task_model = get_task_by_id(db, task.task)
    user = user_service.get_user_by_id(db, task.user)
    new_task_user_exist = db.query(model.TaskUser).filter(model.TaskUser.user == user.id,
                                                          model.TaskUser.task == task_model.id).first()
    if new_task_user_exist:
        raise HTTPException(status_code=409, detail="User already in this task")
    new_task_user = model.TaskUser(**task.dict())
    db.add(new_task_user)
    db.commit()
    db.refresh(new_task_user)

    return task_model


def del_user_from_task(db: Session, taskid: int, userid: int) -> Union[JSONResponse, HTTPException]:
    task = get_task_by_id(db, taskid)
    task_user = db.query(model.TaskUser).filter(model.TaskUser.user == userid, model.TaskUser.task == task.id).first()
    if not task_user:
        raise HTTPException(status_code=404, detail='User is not in task')
    if task_user.is_owner:
        raise HTTPException(status_code=409, detail='Cannot delete a user owner')
    db.delete(task_user)
    db.commit()
    return JSONResponse(status_code=200, content={'message': 'User removed from task'})
