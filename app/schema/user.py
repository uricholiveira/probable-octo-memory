import arrow
from datetime import datetime
from dynaconf import settings
from pydantic import BaseModel, validator
from typing import Optional, List


class UserBase(BaseModel):
	email: str


class UserIn(UserBase):
	name: str
	is_active: Optional[bool]


class UserPatch(BaseModel):
	email: Optional[str]
	name: Optional[str]
	is_active: Optional[str]


class UserRegister(UserIn):
	password: str


class UserOut(UserIn):
	created_at: datetime = None
	is_admin: bool

	@validator("created_at", pre=True)
	def created_at_validate(cls, date):
		return arrow.get(date).to(settings.TIMEZONE).datetime

	class Config:
		orm_mode = True


class TaskUserOut(UserIn):
	id: int
	is_admin: bool

	class Config:
		orm_mode = True