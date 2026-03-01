from fastapi import APIRouter, Depends
from pydantic import EmailStr
from sqlalchemy.orm import Session
from typing import Annotated
from datetime import datetime
from app.database import get_db
from app.core.auth import get_current_active_user
from app.schemas.users import User

router = APIRouter (
    prefix = "/user",
    tags = ["Users"]
)

@router.get('/', response_model=User)
async def get_user(db: Annotated[Session, Depends(get_db)]):
    return (get_current_active_user(db))

@router.post('/register')
async def create(db: Annotated[Session, Depends(get_db)],
    email:EmailStr, hashed_password:str,
    is_active:bool, created_at:datetime):
    return create_user(db=db, email=email, password = hashed_password,
            is_active = is_active, created_at=created_at)


