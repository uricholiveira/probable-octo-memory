from app.ext.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), index=True, unique=True)
    priority_id = Column(Integer, ForeignKey('priority.id'))
    priority = relationship("Priority")
