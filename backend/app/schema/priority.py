from pydantic import BaseModel

from app.schema import task

class PriorityBase(BaseModel):
    description: str

class PriorityOut(PriorityBase):
    task: task.TaskOut

    class Config:
        orm_mode = True