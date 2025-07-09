from email.policy import default

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from app.database.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.employee_crud import (
    get_all_employees,
    get_employee_by_field,
    add_employee,
    update_employee_crud,
    delete_employee_crud
)
from pydantic import EmailStr
from typing import Optional
from app.excepts.exceptions import (
    EmployeeNotFoundException,
    EmailAlreadyExistsException,
    PhoneNumberAlreadyExistsException,
    UsernameAlreadyExistsException
)
from app.Schemas.employee_schema import (
    CreateEmployee,
    UpdateEmployee
)


employee_router = APIRouter()

@employee_router.get('/get-employee/{employee_id}')
async def get_employee(employee_id: int, db: AsyncSession=Depends(get_db)):
    employee = await get_employee_by_field(db, 'id', employee_id)
    if not employee:
        raise EmployeeNotFoundException
    return {
        'success': True,
        'data': employee
    }


@employee_router.get('/get-employees')
async def get_employees(
    search: Optional[str] = None, 
    search_by: Optional[str] = None,
    page:int = 1,
    page_size:int = 10,
    db: AsyncSession=Depends(get_db)
):
    employees = await get_all_employees(
            db=db, page =page, page_size = page_size, search = search, search_by = search_by
        )
    return {
        'success': True,
        'data': employees
    }

@employee_router.post('/create-employee')
async def create_employee(
    employee: CreateEmployee,
    db: AsyncSession=Depends(get_db)
):
    
    await validate_exsits_employee_fields(
        db=db,
        email= employee.email,
        phoneNumber= employee.phoneNumber,
        username= employee.username,
    )

    await add_employee(employee=employee, db=db)

    return JSONResponse(status_code=201, content={
        'success': True,
        'message': 'add employee successfully'
    })

@employee_router.put('/update-employee/{employee_id}')
async def update_employee(employee_id: int, update_employee: UpdateEmployee, db:AsyncSession=Depends(get_db)):
    await validate_exsits_employee_fields(
        email=update_employee.email,
        phoneNumber=update_employee.phoneNumber,
        db=db
    )

    await update_employee_crud(db=db, employee_id=employee_id, employee=update_employee)

    return {
        'success': True,
        'message': 'Update employee successfully'
    }
@employee_router.delete('/delete-employee/{employee_id}')
async def delete_employee(employee_id: int, db: AsyncSession=Depends(get_db)):
    await delete_employee_crud(db, employee_id)
    return {
        'success': True,
        'message': 'Delete employee successfully'
    }

async def validate_exsits_employee_fields(

    db: AsyncSession,
    email: Optional[EmailStr] = None,
    phoneNumber: Optional[str] = None,
    username: Optional[str] = None
):
    if email:
        existsEmail = await get_employee_by_field(db, 'email', email)
        if existsEmail: raise EmailAlreadyExistsException(email)

    if phoneNumber:
        existsPhoneNumber = await get_employee_by_field(db, 'phoneNumber', phoneNumber)
        if existsPhoneNumber: raise PhoneNumberAlreadyExistsException(phoneNumber)

    if username:
        existsUsername = await get_employee_by_field(db, 'username', username)
        if existsUsername: raise UsernameAlreadyExistsException(username)