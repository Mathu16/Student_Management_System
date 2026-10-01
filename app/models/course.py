# Import SQLAlchemy column types
from sqlalchemy import Column, Integer, String, ForeignKey

# Import the Base class used to create database models
from app.db.database import Base


# Create the Course database model
class Course(Base):
    # Define the database table name
    __tablename__ = "courses"

    # Create the primary key column
    id = Column(Integer, primary_key=True, index=True)

    # Store the course name
    course_name = Column(String(100), nullable=False)

    # Store the course code
    course_code = Column(String(50), unique=True, nullable=False, index=True)

    # Store the course description
    description = Column(String(255), nullable=True)

    # Store the ID of the student who is enrolled in this course
    student_id = Column(
        Integer,
        ForeignKey("students.id"),
        nullable=False
    )