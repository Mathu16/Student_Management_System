# Import BaseModel from Pydantic
from pydantic import BaseModel


# Schema used when creating a new student
class StudentCreate(BaseModel):
    # Student's full name
    full_name: str

    # Student's email address
    email: str

    # Student's password
    password: str

    # Student's phone number
    phone: str | None = None


# Schema used when updating student information
class StudentUpdate(BaseModel):
    # Updated student name
    full_name: str | None = None

    # Updated student email
    email: str | None = None

    # Updated student phone number
    phone: str | None = None


# Schema used when returning student information
class StudentResponse(BaseModel):
    # Student ID
    id: int

    # Student's full name
    full_name: str

    # Student's email address
    email: str

    # Student's phone number
    phone: str | None = None