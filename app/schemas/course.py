# Import BaseModel from Pydantic
from pydantic import BaseModel


# Schema used when creating a new course for a student
class CourseCreate(BaseModel):
    # Name of the course
    course_name: str

    # Unique course code
    course_code: str

    # Course description
    description: str | None = None

    # ID of the student who is taking the course
    student_id: int


# Schema used when returning course information
class CourseResponse(BaseModel):
    # Course ID
    id: int

    # Name of the course
    course_name: str

    # Course code
    course_code: str

    # Course description
    description: str | None = None

    # ID of the student who is taking the course
    student_id: int