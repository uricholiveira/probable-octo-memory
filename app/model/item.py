import arrow
from app.ext.db import Base
from passlib.context import CryptContext
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship


class ItemHistory(Base):
    __tablename__ = 'item_history'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    item = Column(Integer, ForeignKey('item.id'))
    items = relationship('Item', back_populates='history')
    value = Column(Float(2), nullable=False)
    created_at = Column(DateTime, nullable=False, default=arrow.utcnow().datetime)
    arrow.get()


class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String(255), index=True, nullable=False)
    value = Column(Float(2), nullable=False)
    task = Column(Integer, ForeignKey('task.id'))
    history = relationship('ItemHistory', back_populates='items')
    created_at = Column(DateTime, nullable=False, default=arrow.utcnow().datetime)
    arrow.get()
    updated_at = Column(DateTime, nullable=True, default=None, onupdate=arrow.utcnow().datetime)