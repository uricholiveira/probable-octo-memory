from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import Union, List

from app.model import annotation as model, task as task_model
from app.schema import annotation as schema
from app.service import task as task_service


def get_all_annotations(db: Session, skip: int = 0, limit: int = 100) -> List[model.Annotation]:
    return db.query(model.Annotation).offset(skip).limit(limit).all()


def get_annotation_by_id(db: Session, annotation_id: int) -> Union[model.Annotation, HTTPException]:
    annotation = db.query(model.Annotation).filter(model.Annotation.id == annotation_id).first()
    if not annotation:
        raise HTTPException(status_code=404, detail='Annotation not found')
    return annotation


def create_new_annotation(db: Session, annotation: schema.AnnotationBase) -> Union[model.Annotation, HTTPException]:
    task_service.get_task_by_id(db, annotation.dict().get('task_id'))
    new_annotation = model.Annotation(**annotation.dict())

    db.add(new_annotation)
    db.commit()
    db.refresh(new_annotation)

    new_task_annotation = task_model.TaskAnnotation(annotation=new_annotation.id, task=new_annotation.task)
    db.add(new_task_annotation)
    db.commit()
    db.refresh(new_annotation)

    return new_annotation


def update_annotation(db: Session, annotation_id: int, annotation: schema.AnnotationBase) -> Union[
    model.Annotation, HTTPException]:
    task_service.get_task_by_id(db, annotation.dict().get('task_id'))
    updated_annotation = get_annotation_by_id(db, annotation_id)
    for field in annotation.dict(exclude_none=True):
        setattr(updated_annotation, field, annotation.dict()[field])
    db.add(updated_annotation)
    db.commit()
    db.refresh(updated_annotation)
    return updated_annotation


def patch_annotation(db: Session, annotation_id: int, annotation: schema.AnnotationPatch) -> Union[
    model.Annotation, HTTPException]:
    task_service.get_task_by_id(db, annotation.dict().get('task_id'))
    updated_annotation = get_annotation_by_id(db, annotation_id)
    for field in annotation.dict(exclude_unset=True, exclude_none=True):
        setattr(updated_annotation, field, annotation.dict()[field])
    db.add(updated_annotation)
    db.commit()
    db.refresh(updated_annotation)
    return updated_annotation


def delete_annotation(db: Session, annotation_id: int) -> Union[JSONResponse, HTTPException]:
    annotation = get_annotation_by_id(db, annotation_id)
    db.delete(annotation)
    db.commit()
    return JSONResponse(status_code=200, content={'detail': 'Annotation deleted'})
