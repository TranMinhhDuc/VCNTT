from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from app.excepts.exceptions import (
    EmployeeNotFoundException, 
    InvalidPaginationException, 
    EmailAlreadyExistsException,
    PhoneNumberAlreadyExistsException,
    UsernameAlreadyExistsException
)
import logging


async def http_exception_handler(request: Request, exc: HTTPException):
    logging.warning(f"HTTP error: {exc.detail}")
    return JSONResponse(status_code=exc.status_code, content={
        'success': False,
        "error": exc.detail
    })

async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
    logging.error(f"Database error: {str(exc)}")
    return JSONResponse(status_code=500, content={'success': False, "error": "Database operation failed"})

async def employee_not_found_handler(request: Request, exc: EmployeeNotFoundException):
    return JSONResponse(
        status_code=404,
        content={'success': False, "error": f"Employee not found"}
    )

async def invalid_pagination_handler(request: Request, exc: InvalidPaginationException):
    return JSONResponse(
        status_code=400,
        content={'success': False, "error": exc.message}
    )

async def fallback_exception_handler(request: Request, exc: Exception):
    logging.exception("Unhandled exception")
    return JSONResponse(
        status_code=500,
        content={'success': False, "error": "Internal Server Error"}
    )

async def email_already_exists_handler(request: Request, exc: EmailAlreadyExistsException):
    return JSONResponse(
        status_code=409,
        content={'success': False, "error": f"Email '{exc.email}' already exists."}
    )

async def phonenumber_already_exists_handler(request: Request, exc: PhoneNumberAlreadyExistsException):
    return JSONResponse(
        status_code=409,
        content={'success': False, "error": f"Phone Number '{exc.phoneNumber}' already exists."}
    )

async def username_already_exists_handler(request: Request, exc: UsernameAlreadyExistsException):
    return JSONResponse(
        status_code=409,
        content={'success': False, "error": f"Username '{exc.username}' already exists."}
    )