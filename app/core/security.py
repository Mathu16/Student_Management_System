# Import CryptContext from Passlib
from passlib.context import CryptContext


# Create a password hashing configuration
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# Hash a plain-text password
def hash_password(password: str) -> str:
    # Return the securely hashed password
    return pwd_context.hash(password)


# Verify a password against its stored hash
def verify_password(password: str, password_hash: str) -> bool:
    # Return True if the password matches the stored hash
    return pwd_context.verify(password, password_hash)