import arrow
from datetime import datetime
from dynaconf import settings
from pydantic import BaseModel, validator
from typing import Optional, List, Union


class ItemHistoryBase(BaseModel):
    id: int
    item: int
    value: float


class ItemHistoryOut(ItemHistoryBase):
    created_at: datetime

    @validator("created_at", pre=True)
    def created_at_validate(cls, date):
        return arrow.get(date).to(settings.TIMEZONE).datetime

    class Config:
        orm_mode = True


class ItemBase(BaseModel):
    description: str
    value: float
    task: int


class ItemPatch(BaseModel):
    description: Optional[str]
    value: Optional[float]


class ItemOut(ItemBase):
    history: List[ItemHistoryOut]

    class Config:
        orm_mode = True
