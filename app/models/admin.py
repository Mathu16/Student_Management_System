# Import SQLAlchemy column types
from sqlalchemy import Column, Integer, String

# Import the Base class used to create database models
from app.db.database import Base


# Create the Admin database model
class Admin(Base):
    # Define the database table name
    __tablename__ = "admins"

    # Create the primary key column
    id = Column(Integer, primary_key=True, index=True)

    # Store the admin username
    username = Column(String(50), unique=True, nullable=False, index=True)

    # Store the hashed admin password
    password_hash = Column(String(255), nullable=False)