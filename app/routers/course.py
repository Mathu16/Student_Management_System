# Import APIRouter and Depends from FastAPI
from fastapi import APIRouter, Depends

# Import Session to work with the database
from sqlalchemy.orm import Session

# Import the database session dependency
from app.db.database import get_db

# Import the Course database model
from app.models.course import Course

# Import the course request and response schemas
from app.schemas.course import CourseCreate, CourseResponse

# Import the admin authentication dependency
from app.core.dependencies import get_current_admin


# Create a router for course-related endpoints
router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)


# Create a new course for a student
@router.post("/", response_model=CourseResponse)
def create_course(
    course_data: CourseCreate,
    db: Session = Depends(get_db),
    current_admin: dict = Depends(get_current_admin)
):
    # Create a new course object
    course = Course(
        course_name=course_data.course_name,
        course_code=course_data.course_code,
        description=course_data.description,
        student_id=course_data.student_id
    )

    # Add the course to the database
    db.add(course)

    # Save the new course
    db.commit()

    # Refresh the course object to get the generated course ID
    db.refresh(course)

    # Print the action in the terminal
    print(
        f"Course created successfully - "
        f"Course: {course.course_name}, "
        f"Student ID: {course.student_id}"
    )

    # Return the created course
    return course

    # Get all courses
@router.get("/", response_model=list[CourseResponse])
def get_all_courses(
    db: Session = Depends(get_db),
    current_admin: dict = Depends(get_current_admin)
):
    # Get all courses from the database
    courses = db.query(Course).all()

    # Print the action in the terminal
    print(
        f"All courses viewed by admin - "
        f"Count: {len(courses)}"
    )

    # Return the list of courses
    return courses