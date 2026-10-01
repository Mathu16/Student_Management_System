# Import BaseModel from Pydantic
from pydantic import BaseModel


# Schema used when creating a new admin
class AdminCreate(BaseModel):
    # Admin username
    username: str

    # Admin password
    password: str


# Schema used when returning admin information
class AdminResponse(BaseModel):
    # Admin ID
    id: int

    # Admin username
    username: str