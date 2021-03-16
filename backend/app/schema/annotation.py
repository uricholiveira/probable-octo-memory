from pydantic import BaseModel

from app.schema import task

class AnnotationBase(BaseModel):
    description: str

class AnnotationOut(AnnotationBase):
    task: task.TaskOut

    class Config:
        orm_mode = True