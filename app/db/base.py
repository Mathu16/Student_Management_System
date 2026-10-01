# Import the Base object from the database configuration
from app.db.database import Base

# Import the Admin model so SQLAlchemy knows about the Admin table
from app.models.admin import Admin

# Import the Student model so SQLAlchemy knows about the Student table
from app.models.student import Student

# Import the Course model so SQLAlchemy knows about the Course table
from app.models.course import Course