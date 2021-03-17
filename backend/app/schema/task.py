import arrow
from datetime import datetime, date
from dynaconf import settings
from pydantic import BaseModel, validator
from typing import Optional, List, Union

from app.schema import user, annotation, situation, category, priority


class TaskBase(BaseModel):
    name: str
    user_owner_id: int
    deadline: Optional[date]


class TaskCreate(TaskBase):
    situation_id: int
    category_id: int


class TaskPatch(BaseModel):
    name: Optional[str]
    user_owner_id: Optional[int]
    deadline: Optional[date]
    situation_id: Optional[int]
    priority_id: Optional[int]
    category_id: Optional[int]


class TaskOut(TaskBase):
    id: int
    deadline: date = None
    users: List[user.TaskUserOut]
    annotations: List[annotation.AnnotationOut]
    situation: situation.SituationOut
    priority: priority.PriorityOut
    category: category.CategoryOut

    @validator("deadline", pre=True)
    def deadline_validate(cls, date):
        if date:
            return arrow.get(date).to(settings.TIMEZONE).date()
        return None

    class Config:
        orm_mode = True


class TaskUserBase(BaseModel):
    user: int
    task: int
