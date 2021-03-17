from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import Union, List

from app.model import priority as model
from app.schema import priority as schema


def get_all_priorities(db: Session, skip: int = 0, limit: int = 100) -> List[model.Priority]:
    return db.query(model.Priority).offset(skip).limit(limit).all()


def get_priority_by_id(db: Session, priority_id: int) -> Union[model.Priority, HTTPException]:
    priority = db.query(model.Priority).filter(model.Priority.id == priority_id).first()
    if not priority:
        raise HTTPException(status_code=404, detail='Priority not found')
    return priority


def create_new_priority(db: Session, priority: schema.PriorityBase) -> Union[model.Priority, HTTPException]:
    new_priority = model.Priority(**priority.dict())

    db.add(new_priority)
    db.commit()
    db.refresh(new_priority)

    return new_priority


def update_priority(db: Session, priority_id: int, priority: schema.PriorityBase) -> Union[
    model.Priority, HTTPException]:
    updated_priority = get_priority_by_id(db, priority_id)
    for field in priority.dict(exclude_none=True):
        setattr(updated_priority, field, priority.dict()[field])
    db.add(updated_priority)
    db.commit()
    db.refresh(updated_priority)
    return updated_priority


def patch_priority(db: Session, priority_id: int, priority: schema.PriorityPatch) -> Union[
    model.Priority, HTTPException]:
    updated_priority = get_priority_by_id(db, priority_id)
    for field in priority.dict(exclude_unset=True, exclude_none=True):
        setattr(updated_priority, field, priority.dict()[field])
    db.add(updated_priority)
    db.commit()
    db.refresh(updated_priority)
    return updated_priority


def delete_priority(db: Session, priority_id: int) -> Union[JSONResponse, HTTPException]:
    priority = get_priority_by_id(db, priority_id)
    db.delete(priority)
    db.commit()
    return JSONResponse(status_code=200, content={'detail': 'Priority deleted'})
