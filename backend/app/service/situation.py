from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import Union, List

from app.model import situation as model
from app.schema import situation as schema


def get_all_situations(db: Session, skip: int = 0, limit: int = 100) -> List[model.Situation]:
    return db.query(model.Situation).offset(skip).limit(limit).all()


def get_situation_by_id(db: Session, situation_id: int) -> Union[model.Situation, HTTPException]:
    situation = db.query(model.Situation).filter(model.Situation.id == situation_id).first()
    if not situation:
        raise HTTPException(status_code=404, detail='Situation not found')
    return situation


def create_new_situation(db: Session, situation: schema.SituationBase) -> Union[model.Situation, HTTPException]:
    new_situation = model.Situation(**situation.dict())

    db.add(new_situation)
    db.commit()
    db.refresh(new_situation)

    return new_situation


def update_situation(db: Session, situation_id: int, situation: schema.SituationBase) -> Union[model.Situation, HTTPException]:
    updated_situation = get_situation_by_id(db, situation_id)
    for field in situation.dict(exclude_none=True):
        setattr(updated_situation, field, situation.dict()[field])
    db.add(updated_situation)
    db.commit()
    db.refresh(updated_situation)
    return updated_situation


def patch_situation(db: Session, situation_id: int, situation: schema.SituationPatch) -> Union[model.Situation, HTTPException]:
    updated_situation = get_situation_by_id(db, situation_id)
    for field in situation.dict(exclude_unset=True, exclude_none=True):
        setattr(updated_situation, field, situation.dict()[field])
    db.add(updated_situation)
    db.commit()
    db.refresh(updated_situation)
    return updated_situation


def delete_situation(db: Session, situation_id: int) -> Union[JSONResponse, HTTPException]:
    situation = get_situation_by_id(db, situation_id)
    db.delete(situation)
    db.commit()
    return JSONResponse(status_code=200, content={'detail': 'Situation deleted'})