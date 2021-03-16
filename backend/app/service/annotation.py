from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import Union, List

from app.model import annotation as model
from app.schema import annotation as schema


def get_all_categories(db: Session, skip: int = 0, limit: int = 100) -> List[model.Annotation]:
    return db.query(model.Annotation).offset(skip).limit(limit).all()


def get_annotation_by_id(db: Session, annotationid: int) -> Union[model.Annotation, HTTPException]:
    annotation = db.query(model.Annotation).filter(model.Annotation.id == annotationid).first()
    if not annotation:
        raise HTTPException(status_code=404, detail='Annotation not found')
    return annotation


def create_new_annotation(db: Session, annotation: schema.AnnotationBase) -> Union[model.Annotation, HTTPException]:
    new_annotation = model.Annotation(**annotation.dict())

    db.add(new_annotation)
    db.commit()
    db.refresh(new_annotation)

    return new_annotation


def update_annotation(db: Session, annotationid: int, annotation: schema.AnnotationBase) -> Union[model.Annotation, HTTPException]:
    updated_annotation = get_annotation_by_id(db, annotationid)
    for field in annotation.dict(exclude_none=True):
        setattr(updated_annotation, field, annotation.dict()[field])
    db.add(updated_annotation)
    db.commit()
    db.refresh(updated_annotation)
    return updated_annotation


def patch_annotation(db: Session, annotationid: int, annotation: schema.AnnotationBase) -> Union[model.Annotation, HTTPException]:
    updated_annotation = get_annotation_by_id(db, annotationid)
    for field in annotation.dict(exclude_unset=True, exclude_none=True):
        setattr(updated_annotation, field, annotation.dict()[field])
    db.add(updated_annotation)
    db.commit()
    db.refresh(updated_annotation)
    return updated_annotation


def delete_annotation(db: Session, annotationid: int) -> Union[JSONResponse, HTTPException]:
    annotation = get_annotation_by_id(db, annotationid)
    db.delete(annotation)
    db.commit()
    return JSONResponse(status_code=200, content={'detail': 'Annotation deleted'})