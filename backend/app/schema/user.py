import arrow
from datetime import datetime
from dynaconf import settings
from pydantic import BaseModel, validator
from typing import Optional, List


class UserBase(BaseModel):
	username: str
	email: str


class UserIn(UserBase):
	name: str
	lastname: str
	is_active: Optional[bool]
	is_admin: Optional[bool]


class UserPatch(BaseModel):
	email: Optional[str]
	name: Optional[str]
	lastname: Optional[str]
	username: str
	is_active: Optional[bool]
	is_admin: Optional[bool]


class UserRegister(UserIn):
	password: str


class UserOut(UserIn):
	id: int
	created_at: datetime = None

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