from app.ext.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Annotation(Base):
    __tablename__ = 'annotation'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String(255), index=True)
    task = Column(Integer, ForeignKey('task.id'))