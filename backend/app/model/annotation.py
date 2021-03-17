from app.ext.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Annotation(Base):
    __tablename__ = 'annotation'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String(255), index=True)
    task_id = Column(Integer, ForeignKey('task.id'))
    task = relationship("Task", back_populates="annotations")