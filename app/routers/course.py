# Import APIRouter and Depends from FastAPI
from fastapi import APIRouter, Depends, HTTPException

# Import Session to work with the database
from sqlalchemy.orm import Session

# Import the database session dependency
from app.db.database import get_db

# Import the Course database model
from app.models.course import Course

# Import the Student database model
from app.models.student import Student

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

     # Check whether the student exists
    student = db.query(Student).filter(
        Student.id == course_data.student_id
    ).first()

    # Reject the request if the student does not exist
    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )


    # Check whether the course code already exists
    existing_course = db.query(Course).filter(
        Course.course_code == course_data.course_code
    ).first()

    # Reject the request if the course code is already registered
    if existing_course:
        raise HTTPException(
            status_code=400,
            detail="Course code already exists"
        )


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

# Get all courses belonging to a specific student
@router.get("/student/{student_id}", response_model=list[CourseResponse])
def get_student_courses(
    student_id: int,
    db: Session = Depends(get_db),
    current_admin: dict = Depends(get_current_admin)
):
    # Get all courses for the specified student
    courses = db.query(Course).filter(
        Course.student_id == student_id
    ).all()

    # Print the action in the terminal
    print(
        f"Student courses viewed by admin - "
        f"Student ID: {student_id}, "
        f"Course Count: {len(courses)}"
    )

    # Return the student's courses
    return courses

# Update an existing course
@router.put("/{course_id}", response_model=CourseResponse)
def update_course(
    course_id: int,
    course_data: CourseCreate,
    db: Session = Depends(get_db),
    current_admin: dict = Depends(get_current_admin)
):
    # Find the course using the provided course ID
    course = db.query(Course).filter(
        Course.id == course_id
    ).first()

    # Check whether the course exists
    if not course:
        from fastapi import HTTPException

        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    # Check whether the new student exists
    student = db.query(Student).filter(
        Student.id == course_data.student_id
    ).first()

    # Reject the request if the student does not exist
    if not student:
        from fastapi import HTTPException

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # Update the course name
    course.course_name = course_data.course_name

    # Update the course code
    course.course_code = course_data.course_code

    # Update the course description
    course.description = course_data.description

    # Update the student assigned to the course
    course.student_id = course_data.student_id

    # Save the changes to the database
    db.commit()

    # Refresh the course object with updated data
    db.refresh(course)

    # Print the action in the terminal
    print(
        f"Course updated successfully - "
        f"ID: {course.id}, "
        f"Course: {course.course_name}"
    )

    # Return the updated course
    return course

    # Delete an existing course
@router.delete("/{course_id}")
def delete_course(
    course_id: int,
    db: Session = Depends(get_db),
    current_admin: dict = Depends(get_current_admin)
):
    # Find the course using the provided course ID
    course = db.query(Course).filter(
        Course.id == course_id
    ).first()

    # Check whether the course exists
    if not course:
        from fastapi import HTTPException

        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    # Save the course name before deleting the record
    course_name = course.course_name

    # Delete the course from the database
    db.delete(course)

    # Save the deletion to the database
    db.commit()

    # Print the action in the terminal
    print(
        f"Course deleted successfully - "
        f"ID: {course_id}, Course: {course_name}"
    )

    # Return a success message
    return {
        "message": "Course deleted successfully"
    }