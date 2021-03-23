from pydantic import BaseModel
from typing import Optional


class AnnotationBase(BaseModel):
    description: str
    task_id: int


class AnnotationPatch(BaseModel):
    description: Optional[str]


class AnnotationOut(AnnotationBase):
    id: int

    class Config:
        orm_mode = True
