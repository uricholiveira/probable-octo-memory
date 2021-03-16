from app.ext.db import Base
from sqlalchemy import Column, Integer, String


class Priority(Base):
    __tablename__ = 'priority'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String(255), index=True)