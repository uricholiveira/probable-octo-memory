import arrow
from datetime import datetime
from dynaconf import settings
from pydantic import BaseModel, validator
from typing import Optional, List, Union

from app.schema import user, item


class TaskBase(BaseModel):
    name: str
    owner: int

class TaskOut(TaskBase):
    users: List[user.TaskUserOut]
    items: List[item.ItemOut]

    class Config:
        orm_mode = True


class TaskUserBase(BaseModel):
    user: int
    task: int
    is_owner: Optional[bool]