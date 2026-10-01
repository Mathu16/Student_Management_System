# Student Management System

A backend REST API for managing student and course information with secure authentication and role-based authorization.

## Technologies Used

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- JWT Authentication
- Passlib
- Swagger / OpenAPI

## Features

### Authentication

- Admin login
- Student login
- JWT-based authentication
- Role-based authorization
- Password hashing using bcrypt

### Student Management

Admin can:

- Create students
- View all students
- View a specific student
- Update student information
- Delete students

Students can:

- View their own profile

### Course Management

Admin can:

- Create courses for students
- View all courses
- View courses belonging to a student
- Update courses
- Delete courses

### Validation

- Prevent duplicate student email addresses
- Prevent duplicate course codes
- Verify that a student exists before assigning a course
- Protect admin-only endpoints from student users

### Terminal Logging

Important actions are printed in the terminal, including:

- Successful login
- Student creation
- Student updates
- Student deletion
- Course creation
- Course updates
- Course deletion
- Data viewing actions

## Project Structure

```text
Student_Management_System/
│
├── app/
│   ├── core/
│   │   ├── dependencies.py
│   │   ├── jwt.py
│   │   └── security.py
│   │
│   ├── db/
│   │   ├── database.py
│   │   └── base.py
│   │
│   ├── models/
│   │   ├── admin.py
│   │   ├── student.py
│   │   └── course.py
│   │
│   ├── routers/
│   │   ├── auth.py
│   │   ├── student.py
│   │   └── course.py
│   │
│   ├── schemas/
│   │   ├── admin.py
│   │   ├── student.py
│   │   └── course.py
│   │
│   └── main.py
│
├── alembic/
├── .env
├── .env.example
├── .gitignore
├── create_admin.py
├── requirements.txt
├── README.md
└── alembic.ini