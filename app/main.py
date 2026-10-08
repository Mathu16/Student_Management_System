# Import FastAPI class from fastapi package
from fastapi import FastAPI

# Import the database engine
from app.db.database import engine

# Import the authentication router
from app.routers.auth import router as auth_router

# Import the student router
from app.routers.student import router as student_router

# Import the course router
from app.routers.course import router as course_router
from fastapi.middleware.cors import CORSMiddleware

# Create a FastAPI application object
app = FastAPI(
    title="Student Data Management System",
    description="Backend API for managing students and courses",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register the authentication router
app.include_router(auth_router)

# Register the student router
app.include_router(student_router)

# Register the course router
app.include_router(course_router)

# Create a GET API endpoint for testing
@app.get("/")
def root():
    # Return a JSON response
    return {
        "message": "Student Management System API is running"
    }

# Create a GET API endpoint to test the PostgreSQL connection
@app.get("/test-db")
def test_database():
    # Try to connect to the PostgreSQL database
    try:
        # Open a connection to the database
        with engine.connect():
            # Print a successful connection message in the terminal
            print("Database connection successful!")

        # Return a successful response to the API client
        return {
            "message": "Database connection successful!"
        }

    # Handle any database connection error
    except Exception as error:
        # Print the actual error in the terminal
        print(f"Database connection failed: {error}")

        # Return the error message to the API client
        return {
            "message": "Database connection failed",
            "error": str(error)
        }