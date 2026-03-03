from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pwdlib import PasswordHash
import jwt
from typing import Annotated
from fastapi import Depends, HTTPException, status
from datetime import datetime, timedelta, timezone
from app.database import get_db
from sqlalchemy.orm import Session      
from pydantic import BaseModel
from app.models.users import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/token")
hash_password = PasswordHash.recommended()
MINUTES_TO_EXPIRE = 30
ALGORITHM = "HS256"
SECRET_KEY="409558a6d0f1871715792050d3ea26236aca096f4ed3e336db532b5bb49dfbe2"

class Token(BaseModel):
    access_token: str
    token_type: str

class UserIn(BaseModel):
    id : int
    email : str
    is_active: bool

def verify_password(plain:str, hashed:str) -> bool:
    try:
        return hash_password.verify(plain, hashed)
    except:
        return False

def password_hash(plain:str):
    return hash_password.hash(plain)

def create_access_token(data:dict, expires: timedelta|None=None):
    encrypt = data.copy()
    if expires:
        exp = datetime.now(timezone.utc)+ expires
    else:
        exp = datetime.now(timezone.utc) + timedelta(minutes=15)
    encrypt.update({"exp":exp})
    token = jwt.encode(encrypt, SECRET_KEY, algorithm=ALGORITHM)
    return token

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)],
    db:Session= Depends(get_db)):

    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
    detail = "Could not validate credentials",
    headers = {"WWW-Authenticate":"Bearer"})
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username = payload.get("sub")
    if username is None:
        raise credentials_exception
    user = db.query(User).filter(username == User.email).first()
    if user is None:
        raise credentials_exception
    return user

def get_current_active_user(user:Annotated[User, Depends(get_current_user)],
    db:Session=Depends(get_db)):
    if not user.is_active:
        raise HTTPException(status_code=403, detail="Inactive user")
    return user


def login(formdata: Annotated[OAuth2PasswordRequestForm, Depends()], db:
    Annotated[Session, Depends(get_db)]):
    user = db.query(User).filter(User.email == formdata.username).first()
   
    if user is None:
        raise HTTPException(status_code=404, detail="Not Found")
    if verify_password(formdata.password, user.hashed_password):
        expire = timedelta(minutes=20)
        token_str = create_access_token(
            {"sub":user.email}, expires = expire)
        return Token(access_token=token_str, token_type="Bearer") 
    raise HTTPException(status_code=401, detail="Unauthorized")