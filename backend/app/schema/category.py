from pydantic import BaseModel

from app.schema import priority

class CategoryBase(BaseModel):
    description: str
    default_priority: int

class CategoryOut(CategoryBase):
    priority: priority.PriorityOut

    class Config:
        orm_mode = True