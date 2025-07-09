from typing import Optional
from pydantic import BaseModel, EmailStr
from app.models.model_employee import RoleEnum

class EmployeeBase(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phoneNumber: Optional[str] = None

    class config:
        orm_mode = True

class CreateEmployee(EmployeeBase):
    name: str
    email: EmailStr
    phoneNumber: str
    username: str
    password: str

class UpdateEmployee(EmployeeBase):
    password: Optional[str] = None
    role: Optional[RoleEnum] = None

class DeleteEmployee(BaseModel):
    id: int

