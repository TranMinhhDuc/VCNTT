from os.path import exists

from sqlalchemy.ext.asyncio import AsyncSession
from app.Schemas.employee_schema import CreateEmployee, UpdateEmployee, DeleteEmployee
from app.excepts.exceptions import EmployeeNotFoundException
from app.utils.security import hash_password
from sqlalchemy import func
from sqlalchemy.future import select
from app.models.model_employee import Employee 
from fastapi import HTTPException

async  def get_employee_by_field(db:AsyncSession, field_name:str, value) :
    column_attr = getattr(Employee, field_name)
    stmt = select(
        Employee.id,
        Employee.name,
        Employee.phoneNumber,
        Employee.email,
        Employee.username,
        Employee.role
    ).where(column_attr.__eq__(value)).limit(1)

    result = await db.execute(stmt)
    employee = result.first()
    if not employee: return None
    return {
        'id': employee.id,
        'name': employee.name,
        'phoneNumber': employee.phoneNumber,
        'email': employee.email,
        'username': employee.username,
        'role': employee.role
    }

async def get_all_employees(
    db: AsyncSession, 
    page: int = 1, 
    page_size: int = 10, 
    search: str = None,
    search_by: str = None
):
    if page < 1 or page_size < 1:
        raise HTTPException(status_code=400, detail="Page and page_size must be greater than 0")

    offset = (page - 1) * page_size

    base_query = select(
        Employee.id,
        Employee.name,
        Employee.phoneNumber,
        Employee.email,
        Employee.username,
        Employee.role
    )

    if search and search_by:
        search_value = f"%{search}%"

        if hasattr(Employee, search_by):
            column_attr = getattr(Employee, search_by)
            base_query = base_query.where(column_attr.ilike(search_value))
        else:
            raise HTTPException(status_code=400, detail=f"Invalid search_by field: {search_by}")

    count_query = base_query.with_only_columns(func.count()).order_by(None)
    total_result = await db.execute(count_query)
    total_employee = total_result.scalar()

    stmt = base_query.offset(offset).limit(page_size)
    result = await db.execute(stmt)
    rows = result.all()
    if not len(rows) > 0 : raise EmployeeNotFoundException
    total_pages = (total_employee + page_size - 1) // page_size
    employees = []

    for row in rows:
        employees.append({
            'id': row[0],
            'name': row[1],
            'phoneNumber': row[2],
            'email': row[3],
            'username': row[4],
            'role': row[5]
        })
    return {
        "totalEmployee": total_employee,
        "totalPages": total_pages,
        "currentPage": page,
        "pageSize": page_size,
        "employees": employees
    }

async def add_employee(db: AsyncSession, employee: CreateEmployee):
    try:

        hashed_password = hash_password(employee.password)
        new_employee = Employee(
            name = employee.name,
            email = employee.email,
            phoneNumber = employee.phoneNumber,
            username = employee.username,
            password = hashed_password
        )
        db.add(new_employee)
        await db.commit()
        await db.refresh(new_employee)
        return new_employee
    
    except Exception as e:
        await db.rollback()
        raise e

async def update_employee_crud(db: AsyncSession, employee_id: int, employee: UpdateEmployee):
    try:
        stmt = select(Employee).where(Employee.id == employee_id)
        result = await db.execute(stmt)
        exists_employee = result.scalar_one_or_none()

        if not exists_employee:
            raise EmployeeNotFoundException

        for key, value in employee.dict(exclude_unset=True).items():
            setattr(exists_employee, key, value)

        await db.commit()
        await db.refresh(exists_employee)
        return exists_employee
    except Exception as e:
        await db.rollback()
        raise e


async def delete_employee_crud(db: AsyncSession, employee_id: int):
    try:
        stmt = select(Employee).where(Employee.id == employee_id)
        result = await db.execute(stmt)
        exists_employee = result.scalar_one_or_none()

        if not exists_employee:
            raise EmployeeNotFoundException(f"Employee with ID {employee_id} not found.")

        await db.delete(exists_employee)
        await db.commit()
        return {"detail": f"Employee with ID {employee_id} has been deleted successfully."}
    except Exception as e:
        await db.rollback()
        raise e