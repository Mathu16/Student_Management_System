# Import Depends to use FastAPI dependency injection
from fastapi import Depends

# Import HTTPException to return authentication errors
from fastapi import HTTPException

# Import status codes used by FastAPI
from fastapi import status

# Import OAuth2PasswordBearer to read the JWT token
from fastapi.security import OAuth2PasswordBearer

# Import JWTError to handle invalid JWT tokens
from jose import JWTError

# Import our JWT decoding function
from app.core.jwt import decode_access_token


# Tell FastAPI where users will obtain their login token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


# Get the current authenticated user from the JWT token
def get_current_user(token: str = Depends(oauth2_scheme)):
    # Try to decode and verify the JWT token
    try:
        # Decode the JWT token
        payload = decode_access_token(token)

        # Return the information stored inside the token
        return payload

    # Handle an invalid or expired JWT token
    except JWTError:
        # Return an authentication error
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired authentication token",
            headers={"WWW-Authenticate": "Bearer"},
        )

# Check whether the authenticated user is an admin
def get_current_admin(
    current_user: dict = Depends(get_current_user)
):
    # Check the role stored in the JWT token
    if current_user.get("role") != "admin":
        # Reject the request when the user is not an admin
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )

    # Return the authenticated admin information
    return current_user

    # Check whether the authenticated user is a student
def get_current_student(
    current_user: dict = Depends(get_current_user)
):
    # Check the role stored in the JWT token
    if current_user.get("role") != "student":
        # Reject the request when the user is not a student
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Student access required"
        )

    # Return the authenticated student information
    return current_user