from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import Union, List

from app.model import item as model, task as task_model
from app.schema import item as schema
from app.service import authentication as authentication_service, task as task_service


def get_all_items(db: Session, skip: int = 0, limit: int = 0) -> Union[List[model.Item], HTTPException]:
    items = db.query(model.Item).offset(skip).limit(limit).all()
    if not items:
        raise HTTPException(status_code=404, detail='No one items had found')
    return items


def get_item_by_id(db: Session, itemid: int) -> Union[model.Item, HTTPException]:
    item = db.query(model.Item).filter(model.Item.id == itemid).first()
    if not item:
        raise HTTPException(status_code=404, detail='Item not found')
    return item


def create_new_item(db: Session, item: schema.ItemBase) -> model.Item:
    new_item = model.Item(**item.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    new_item_history = model.ItemHistory(item=new_item.id, value=new_item.value)
    db.add(new_item_history)
    db.commit()
    db.refresh(new_item_history)

    return new_item


def update_item(db: Session, itemid: int, item: schema.ItemBase) -> Union[model.Item, HTTPException]:
    new_item = get_item_by_id(db, itemid)
    for field, value in item.dict(exclude_none=True):
        setattr(new_item, field, value)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    new_item_history = model.ItemHistory(item=new_item.id, value=new_item.value)
    db.add(new_item_history)
    db.commit()
    db.refresh(new_item_history)
    return new_item


def patch_item(db: Session, itemid: int, item: schema.ItemPatch) -> Union[model.Item, HTTPException]:
    new_item = get_item_by_id(db, itemid)
    for field in item.dict(exclude_none=True, exclude_unset=True):
        setattr(new_item, field, item.dict()[field])
    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    new_item_history = model.ItemHistory(item=new_item.id, value=new_item.value)
    db.add(new_item_history)
    db.commit()
    db.refresh(new_item_history)
    return new_item


def delete_item(db: Session, itemid: int, user) -> Union[JSONResponse, HTTPException]:
    item = get_item_by_id(db, itemid)
    item_history = db.query(model.ItemHistory).filter(model.ItemHistory.item == item.id).delete()
    db.delete(item)
    db.commit()
    return JSONResponse(status_code=200, content='Item deleted')
