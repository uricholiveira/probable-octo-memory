from app.ext.db import Base
from sqlalchemy import Column, Integer, String


class Situation(Base):
    __tablename__ = 'situation'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String(255), index=True)