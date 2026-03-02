from sqlalchemy.orm import Session
from app.database import get_db
from pydantic import EmailStr
from datetime import datetime, timezone
from app.models.users import User
from app.core.auth import password_hash

def create_user(db:Session, email:EmailStr, password:str, 
    is_active:bool, created_at:datetime ):

    user = User(email=email, hashed_password=password_hash(password),
    is_active=is_active, created_at=datetime.now(timezone.utc))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user