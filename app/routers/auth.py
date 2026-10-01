# Import APIRouter and HTTPException from FastAPI
from fastapi import APIRouter, HTTPException

# Import the database session dependency
from app.db.database import get_db

# Import the Admin database model
from app.models.admin import Admin

# Import the Student database model
from app.models.student import Student

# Import the password verification function
from app.core.security import verify_password

# Import the JWT token creation function
from app.core.jwt import create_access_token

# Import Depends for database dependency injection
from fastapi import Depends

# Import Session from SQLAlchemy
from sqlalchemy.orm import Session


# Create a router for authentication-related endpoints
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# Create the login endpoint
@router.post("/login")
def login(
    username: str,
    password: str,
    db: Session = Depends(get_db)
):
    # First, search for an admin using the provided username
    admin = db.query(Admin).filter(
        Admin.username == username
    ).first()

    # Check whether the admin exists and the password is correct
    if admin and verify_password(password, admin.password_hash):

        # Create a JWT token containing the admin ID and role
        token = create_access_token({
            "user_id": admin.id,
            "role": "admin"
        })

        # Print the successful login action in the terminal
        print(f"Admin login successful: {admin.username}")

        # Return the access token
        return {
            "access_token": token,
            "token_type": "bearer",
            "role": "admin"
        }


    # Search for a student using the provided email address
    student = db.query(Student).filter(
        Student.email == username
    ).first()

    # Check whether the student exists and the password is correct
    if student and verify_password(password, student.password_hash):

        # Create a JWT token containing the student ID and role
        token = create_access_token({
            "user_id": student.id,
            "role": "student"
        })

        # Print the successful login action in the terminal
        print(f"Student login successful: {student.email}")

        # Return the access token
        return {
            "access_token": token,
            "token_type": "bearer",
            "role": "student"
        }


    # Return an error when the username/password is incorrect
    raise HTTPException(
        status_code=401,
        detail="Invalid username or password"
    )