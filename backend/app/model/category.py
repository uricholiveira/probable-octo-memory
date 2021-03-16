from app.ext.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), index=True)
    default_priority = Column(Integer, ForeignKey('priority.id'))