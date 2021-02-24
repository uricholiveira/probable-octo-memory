import arrow
from app.ext.db import Base
from passlib.context import CryptContext
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

crypt = CryptContext(schemes=['bcrypt'], deprecated='auto')


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    # lastname = Column(String(255), nullable=True)
    email = Column(String(255), nullable=False, index=True, unique=True)
    passw = Column(String(255), nullable=False, name='password')
    created_at = Column(DateTime, nullable=False, default=arrow.utcnow().datetime)
    arrow.get()
    updated_at = Column(DateTime, nullable=True, default=None, onupdate=arrow.utcnow().datetime)
    is_active = Column(Boolean, nullable=False, default=True)
    is_admin = Column(Boolean, nullable=False, default=False)
    tasks = relationship("Task", secondary="task_user", back_populates="users")

    @property
    def password(self):
        return self.passw

    @password.setter
    def password(self, value):
        self.passw = crypt.hash(value)

    def check_password(self, value):
        return crypt.verify(value, self.password)
