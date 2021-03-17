from pydantic import BaseModel
from typing import Optional


class PriorityBase(BaseModel):
    description: str


class PriorityPatch(BaseModel):
    description: Optional[str]


class PriorityOut(PriorityBase):
    id: int
    class Config:
        orm_mode = True
