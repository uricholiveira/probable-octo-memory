from pydantic import BaseModel
from typing import Optional


class SituationBase(BaseModel):
    description: str


class SituationPatch(BaseModel):
    description: Optional[str]


class SituationOut(SituationBase):
    id: int
    class Config:
        orm_mode = True
