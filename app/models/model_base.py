from datetime import datetime
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class ModelBase(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    createDate = Column(DateTime, default=datetime.now)
    updateDate = Column(DateTime, default=datetime.now, onupdate=datetime.now)
