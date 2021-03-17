from pydantic import BaseModel
from typing import Optional

from app.schema import priority


class CategoryBase(BaseModel):
    name: str
    priority_id: int


class CategoryPatch(BaseModel):
    name: Optional[int]
    priority_id: Optional[int]


class CategoryOut(CategoryBase):
    id: int
    priority: priority.PriorityOut

    class Config:
        orm_mode = True
