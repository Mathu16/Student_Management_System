# Import os to read environment variables
import os

# Import load_dotenv to load variables from the .env file
from dotenv import load_dotenv

# Import SQLAlchemy components for database connection
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Load variables from the .env file
load_dotenv()

# Get the PostgreSQL database URL from the environment
DATABASE_URL = os.getenv("DATABASE_URL")

# Create the SQLAlchemy database engine
engine = create_engine(DATABASE_URL)

# Create a database session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Create the base class for our database models
Base = declarative_base()


# Create a function that provides a database session
def get_db():
    # Create a new database session
    db = SessionLocal()

    try:
        # Give the database session to the API endpoint
        yield db

    finally:
        # Close the database session after the request is finished
        db.close()