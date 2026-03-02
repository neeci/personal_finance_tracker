from fastapi import APIRouter, Depends
from pydantic import EmailStr
from sqlalchemy.orm import Session
from typing import Annotated
from datetime import datetime
from app.database import get_db
from app.core.auth import get_current_active_user, login
from app.schemas.users import User, UserResponse
from app.crud.users import create_user
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter (
    prefix = "/user",
    tags = ["Users"]
)

@router.get('/', response_model=UserResponse)
async def get_user(db: Annotated[Session, Depends(get_db)],
    user: User = Depends(get_current_active_user)):
    return (user)

@router.post('/register', response_model=UserResponse)
async def create(db: Annotated[Session, Depends(get_db)],
    email:EmailStr, hashed_password:str,
    is_active:bool):
    return create_user(db=db, email=email, password = hashed_password,
            is_active = is_active, created_at = None)

@router.post('/token')
async def login_access(form_data: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(get_db)):
    return login(db=db, formdata=form_data)


