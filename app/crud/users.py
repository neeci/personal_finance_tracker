from sqlalchemy.orm import Session
from app.database import get_db
from pydantic import EmailStr
from datetime import datetime
from app.models.user import User
from app.core.auth import hash_password

def create_user(db:Session, email:EmailStr, password:str, 
    is_active:bool, created_at:datetime ):

    user = User(email=email, hashed_password=hash_password(password),
    is_active=is_active, created_at:datetime.now)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user