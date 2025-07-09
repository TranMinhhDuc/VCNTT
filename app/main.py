from fastapi import FastAPI
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.excepts.exceptions import (
    EmployeeNotFoundException, 
    InvalidPaginationException, 
    EmailAlreadyExistsException,
    PhoneNumberAlreadyExistsException,
    UsernameAlreadyExistsException
)
from app.excepts.exception_handler import (
    http_exception_handler,
    sqlalchemy_exception_handler,
    employee_not_found_handler,
    invalid_pagination_handler,
    fallback_exception_handler,
    email_already_exists_handler,
    phonenumber_already_exists_handler,
    username_already_exists_handler
)

from app.api.employee_api import employee_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(SQLAlchemyError, sqlalchemy_exception_handler)
app.add_exception_handler(EmployeeNotFoundException, employee_not_found_handler)
app.add_exception_handler(InvalidPaginationException, invalid_pagination_handler)
app.add_exception_handler(Exception, fallback_exception_handler)
app.add_exception_handler(EmailAlreadyExistsException, email_already_exists_handler)
app.add_exception_handler(PhoneNumberAlreadyExistsException, phonenumber_already_exists_handler)
app.add_exception_handler(UsernameAlreadyExistsException, username_already_exists_handler)

app.include_router(employee_router)