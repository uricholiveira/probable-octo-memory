from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import Union, List

from app.model import category as model
from app.schema import category as schema


def get_all_categories(db: Session, skip: int = 0, limit: int = 100) -> List[model.Category]:
    return db.query(model.Category).offset(skip).limit(limit).all()


def get_category_by_id(db: Session, categoryid: int) -> Union[model.Category, HTTPException]:
    category = db.query(model.Category).filter(model.Category.id == categoryid).first()
    if not category:
        raise HTTPException(status_code=404, detail='Category not found')
    return category


def create_new_category(db: Session, category: schema.CategoryBase) -> Union[model.Category, HTTPException]:
    new_category = model.Category(**category.dict())

    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category


def update_category(db: Session, categoryid: int, category: schema.CategoryBase) -> Union[model.Category, HTTPException]:
    updated_category = get_category_by_id(db, categoryid)
    for field in category.dict(exclude_none=True):
        setattr(updated_category, field, category.dict()[field])
    db.add(updated_category)
    db.commit()
    db.refresh(updated_category)
    return updated_category


def patch_category(db: Session, categoryid: int, category: schema.CategoryBase) -> Union[model.Category, HTTPException]:
    updated_category = get_category_by_id(db, categoryid)
    for field in category.dict(exclude_unset=True, exclude_none=True):
        setattr(updated_category, field, category.dict()[field])
    db.add(updated_category)
    db.commit()
    db.refresh(updated_category)
    return updated_category


def delete_category(db: Session, categoryid: int) -> Union[JSONResponse, HTTPException]:
    category = get_category_by_id(db, categoryid)
    db.delete(category)
    db.commit()
    return JSONResponse(status_code=200, content={'detail': 'Category deleted'})