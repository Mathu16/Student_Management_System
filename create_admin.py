# Import the database session
from app.db.database import SessionLocal

# Import the Admin database model
from app.models.admin import Admin

# Import the password hashing function
from app.core.security import hash_password


# Create a database session
db = SessionLocal()

try:
    # Create a new admin account
    admin = Admin(
        username="admin",
        password_hash=hash_password("admin123")
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