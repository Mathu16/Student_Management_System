# Import FastAPI class from fastapi package
from fastapi import FastAPI


# Create a FastAPI application object
app = FastAPI(
    title="Student Data Management System",
    description="Backend API for managing students and courses",
    version="1.0.0"
)


# Create a GET API endpoint for testing
@app.get("/")
def root():
    # Return a JSON response
    return {
        "message": "Student Management System API is running"
    }