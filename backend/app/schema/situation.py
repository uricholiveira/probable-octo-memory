from pydantic import BaseModel

class SituationBase(BaseModel):
    description: str

class SituationOut(SituationBase):
    class Config:
        orm_mode = True