# Import SQLAlchemy column types
from sqlalchemy import Column, Integer, String

# Import the Base class used to create database models
from app.db.database import Base


# Create the Student database model
class Student(Base):
    # Define the database table name
    __tablename__ = "students"

    # Create the primary key column
    id = Column(Integer, primary_key=True, index=True)

    # Store the student's full name
    full_name = Column(String(100), nullable=False)

    # Store the student's email address
    email = Column(String(100), unique=True, nullable=False, index=True)

    # Store the student's password hash
    password_hash = Column(String(255), nullable=False)

    # Store the student's contact number
    phone = Column(String(20), nullable=True)