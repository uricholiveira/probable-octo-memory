import arrow
from datetime import datetime
from dynaconf import settings
from pydantic import BaseModel, validator
from typing import Optional, List, Union

from app.schema import user


class TaskBase(BaseModel):
    name: str
    owner: int
    deadline: Optional[datetime]

class TaskOut(TaskBase):
    users: List[user.TaskUserOut]

    @validator("deadline", pre=True)
	def created_at_validate(cls, date):
		return arrow.get(date).to(settings.TIMEZONE).datetime

    class Config:
        orm_mode = True

class TaskUserBase(BaseModel):
    user: int
    task: int
    is_owner: Optional[bool]