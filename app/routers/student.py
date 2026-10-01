# Import APIRouter and Depends from FastAPI
from fastapi import APIRouter, Depends

# Import Session to work with the database
from sqlalchemy.orm import Session

# Import the database session dependency
from app.db.database import get_db

# Import the Student database model
from app.models.student import Student

# Import the student request and response schemas
from app.schemas.student import StudentCreate, StudentUpdate, StudentResponse

# Import the admin authentication dependency
from app.core.dependencies import get_current_admin, get_current_student

# Import the password hashing function
from app.core.security import hash_password


# Create a router for student-related endpoints
router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


# Create a new student
@router.post("/", response_model=StudentResponse)
def create_student(
    student_data: StudentCreate,
    db: Session = Depends(get_db),
    current_admin: dict = Depends(get_current_admin)
):
    # Create a new student object
    student = Student(
        full_name=student_data.full_name,
        email=student_data.email,
        password_hash=hash_password(student_data.password),
        phone=student_data.phone
    )

    # Add the student to the database
    db.add(student)

    # Save the new student
    db.commit()

    # Refresh the student object to get the generated ID
    db.refresh(student)

    # Print the action in the terminal
    print(
        f"Student created successfully - "
        f"ID: {student.id}, Email: {student.email}"
    )

    # Return the created student
    return student
# Get the profile of the currently logged-in student
@router.get("/me", response_model=StudentResponse)
def get_my_profile(
    db: Session = Depends(get_db),
    current_student: dict = Depends(get_current_student)
):
    # Get the student ID from the JWT token
    student_id = current_student.get("user_id")

    # Find the student using the ID from the token
    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    # Check whether the student exists
    if not student:
        # Return an error if the student was not found
        from fastapi import HTTPException

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # Print the action in the terminal
    print(
        f"Student viewed own profile - "
        f"ID: {student.id}, Email: {student.email}"
    )

    # Return the student's own profile
    return student


# Get all students
@router.get("/", response_model=list[StudentResponse])
def get_all_students(
    db: Session = Depends(get_db),
    current_admin: dict = Depends(get_current_admin)
):
    # Get all students from the database
    students = db.query(Student).all()

    # Print the action in the terminal
    print(
        f"All students viewed by admin - "
        f"Count: {len(students)}"
    )

    # Return the list of students
    return students

# Get a single student by ID
@router.get("/{student_id}", response_model=StudentResponse)
def get_student_by_id(
    student_id: int,
    db: Session = Depends(get_db),
    current_admin: dict = Depends(get_current_admin)
):
    # Find the student using the provided student ID
    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    # Check whether the student exists
    if not student:
        # Return an error if the student was not found
        from fastapi import HTTPException

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # Print the action in the terminal
    print(
        f"Student viewed by admin - "
        f"ID: {student.id}, Email: {student.email}"
    )

    # Return the student information
    return student

# Update an existing student
@router.put("/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int,
    student_data: StudentUpdate,
    db: Session = Depends(get_db),
    current_admin: dict = Depends(get_current_admin)
):
    # Find the student using the provided student ID
    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    # Check whether the student exists
    if not student:
        # Return an error if the student was not found
        from fastapi import HTTPException

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # Update the student's name if a new name was provided
    if student_data.full_name is not None:
        student.full_name = student_data.full_name

    # Update the student's email if a new email was provided
    if student_data.email is not None:
        student.email = student_data.email

    # Update the student's phone if a new phone number was provided
    if student_data.phone is not None:
        student.phone = student_data.phone

    # Save the changes to the database
    db.commit()

    # Refresh the student object with the updated data
    db.refresh(student)

    # Print the action in the terminal
    print(
        f"Student updated successfully - "
        f"ID: {student.id}, Email: {student.email}"
    )

    # Return the updated student
    return student

# Delete an existing student
@router.delete("/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db),
    current_admin: dict = Depends(get_current_admin)
):
    # Find the student using the provided student ID
    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    # Check whether the student exists
    if not student:
        # Return an error if the student was not found
        from fastapi import HTTPException

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # Save the student's email before deleting the record
    student_email = student.email

    # Delete the student from the database
    db.delete(student)

    # Save the deletion to the database
    db.commit()

    # Print the action in the terminal
    print(
        f"Student deleted successfully - "
        f"ID: {student_id}, Email: {student_email}"
    )

    # Return a success message
    return {
        "message": "Student deleted successfully"
    }

