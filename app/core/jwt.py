# Import os to read environment variables
import os

# Import datetime tools for token expiration
from datetime import datetime, timedelta, timezone

# Import JWT functions from python-jose
from jose import jwt

# Import load_dotenv to load variables from the .env file
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()


# Get the JWT secret key from the environment
JWT_SECRET = os.getenv("JWT_SECRET")

# Get the JWT algorithm from the environment
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

# Get the token expiration time from the environment
ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30")
)


# Create a new JWT access token
def create_access_token(data: dict) -> str:
    # Make a copy of the data so the original data is not changed
    to_encode = data.copy()

    # Calculate when the token should expire
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    # Add the expiration time to the token data
    to_encode.update({"exp": expire})

    # Create and return the JWT token
    return jwt.encode(
        to_encode,
        JWT_SECRET,
        algorithm=JWT_ALGORITHM
    )


# Decode and verify a JWT access token
def decode_access_token(token: str) -> dict:
    # Decode the token using our secret key and algorithm
    payload = jwt.decode(
        token,
        JWT_SECRET,
        algorithms=[JWT_ALGORITHM]
    )

    # Return the information stored inside the token
    return payload