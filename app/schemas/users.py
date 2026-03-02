from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserResponse(BaseModel):
    id:int
    email: EmailStr
    created_at: datetime

class User(BaseModel):
    id:int
    email: EmailStr
    created_at: datetime
    is_active: bool
    hashed_password: str