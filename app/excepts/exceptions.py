class EmployeeNotFoundException(Exception):
    pass


class InvalidPaginationException(Exception):
    def __init__(self, message: str = "Page and page_size must be greater than 0"):
        self.message = message

class EmailAlreadyExistsException(Exception):
    def __init__(self, email: str):
        self.email = email

class PhoneNumberAlreadyExistsException(Exception):
    def __init__(self, phoneNumber: str):
        self.phoneNumber = phoneNumber

class UsernameAlreadyExistsException(Exception):
    def __init__(self, username: str):
        self.username = username
