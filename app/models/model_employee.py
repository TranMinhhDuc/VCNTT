from app.models.model_base import ModelBase
from sqlalchemy import Column, String, Enum
import enum

class RoleEnum(enum.Enum):
    manager = "manager"
    staff = "staff"

class Employee(ModelBase):
    __tablename__ = 'employee'

    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phoneNumber = Column(String, nullable=False, unique=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    role = Column(Enum(RoleEnum), default=RoleEnum.staff)