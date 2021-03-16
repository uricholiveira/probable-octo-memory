from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.ext.db import get_db
from app.service import annotation as service, authentication as authentication_service
from app.schema import annotation as schema, authentication as authentication_schema

router = APIRouter(prefix='/annotation', tags=['Annotation'])


@router.get('/', response_model=List[schema.AnnotationOut], description='Get list of all annotations')
def get_all_annotations(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return service.get_all_annotations(db=db, skip=skip, limit=limit)


@router.get('/', response_model=schema.AnnotationOut, description='Get annotation by ID')
def get_annotation_by_id(db: Session = Depends(get_db), annotationid: int = None):
    return service.get_annotation_by_id(db, annotationid)


@router.post('/', response_model=schema.AnnotationOut, description='Create a new annotation')
def create_new_annotation(db: Session = Depends(get_db), annotation: schema.AnnotationBase = Depends()):
    return service.create_new_annotation(db, annotation)


@router.put('/', response_model=schema.AnnotationOut, description='Update annotation')
def update_annotation(db: Session = Depends(get_db), annotationid: int = 0, annotation: schema.AnnotationBase = Depends()):
    return service.update_annotation(db, annotationid, annotation)


@router.patch('/', response_model=schema.AnnotationOut, description='Update annotation fields')
def patch_annotation(db: Session = Depends(get_db), annotationid: int = 0, annotation: schema.AnnotationBase = Depends()):
    return service.patch_annotation(db, annotationid, annotation)


@router.delete('/', description='Delete annotation', responses={200: {'detail': 'Annotation deleted'}},
               dependencies=[Depends(authentication_service.oauth2_schema)])
def delete_annotation(db: Session = Depends(get_db), annotationid: int = 0):
    return service.delete_annotation(db, annotationid)