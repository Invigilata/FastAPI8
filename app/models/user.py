from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.backend.db import Base
from app.models.task import Task  # Это нужно для создания отношений

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    tasks = relationship("Task", back_populates="user")
