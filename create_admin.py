# Import os to read environment variables
import os

# Import load_dotenv to load variables from the .env file
from dotenv import load_dotenv

# Import the database session
from app.db.database import SessionLocal

# Import the Admin database model
from app.models.admin import Admin

# Import the password hashing function
from app.core.security import hash_password


# Load environment variables from the .env file
load_dotenv()


# Get the admin username from the environment
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")

# Get the admin password from the environment
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")


# Create a database session
db = SessionLocal()

try:
    # Create a new admin account
    admin = Admin(
        username=ADMIN_USERNAME,
        password_hash=hash_password(ADMIN_PASSWORD)
    )

    # Add the admin to the database
    db.add(admin)

    # Save the admin record
    db.commit()

    # Print a success message in the terminal
    print("Admin account created successfully!")

finally:
    # Close the database session
    db.close()