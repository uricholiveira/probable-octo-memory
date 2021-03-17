from sqlalchemy.sql.expression import null
import arrow
from app.ext.db import Base
from passlib.context import CryptContext
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Date
from sqlalchemy.orm import relationship


class TaskUser(Base):
    __tablename__ = 'task_user'
    user = Column(Integer, ForeignKey('user.id'), primary_key=True)
    task = Column(Integer, ForeignKey('task.id'), primary_key=True)

# class TaskCategory(Base):
#     __tablename__ = 'task_category'
#     category = Column(Integer, ForeignKey('category.id'), primary_key=True)
#     task = Column(Integer, ForeignKey('task.id'), primary_key=True)

# class TaskPriority(Base):
#     __tablename__ = 'task_priority'
#     priority = Column(Integer, ForeignKey('priority.id'), primary_key=True)
#     task = Column(Integer, ForeignKey('task.id'), primary_key=True)

# class TaskSituation(Base):
#     __tablename__ = 'task_situation'
#     situation = Column(Integer, ForeignKey('situation.id'), primary_key=True)
#     task = Column(Integer, ForeignKey('task.id'), primary_key=True)

class TaskAnnotation(Base):
    __tablename__ = 'task_annotation'
    annotation = Column(Integer, ForeignKey('annotation.id'), primary_key=True)
    task = Column(Integer, ForeignKey('task.id'), primary_key=True)


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), index=True)
    user_owner_id = Column(Integer, ForeignKey('user.id'))
    priority_id = Column(Integer, ForeignKey('priority.id'))
    category_id = Column(Integer, ForeignKey('category.id'))
    situation_id = Column(Integer, ForeignKey('situation.id'))
    deadline = Column(Date, nullable=True, default=None)
    created_at = Column(DateTime, nullable=False, default=arrow.utcnow().datetime)
    arrow.get()
    updated_at = Column(DateTime, nullable=True, default=None, onupdate=arrow.utcnow().datetime)
    users = relationship("User", secondary="task_user", back_populates="tasks")
    annotations = relationship("Annotation", secondary="task_annotation")
    priority = relationship("Priority")
    category = relationship("Category")
    situation = relationship("Situation")
