from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from app.database import get_db
from app.schemas.users import User
from app.schemas.accounts import Account, AccountResponse
from app.core.auth import get_current_active_user
from app.crud.accounts import create, accounts
from app.schemas.accounts import AccountNameEnum

router = APIRouter (
    prefix = "/account",
    tags = ["Account"]
)

@router.post('/create', response_model=Account)
async def create_account(name:AccountNameEnum, balance:int, db:Session = Depends(get_db), 
user:User=Depends(get_current_active_user) ):
    return create(db=db, user_id = user.id, name=name, balance=balance,
    created_at=datetime.utcnow())

@router.get('/list', response_model=list[AccountResponse])
async def getAccounts(user:User=Depends(get_current_active_user), 
db:Session = Depends(get_db)):
    return accounts(db=db, user_id=user.id)

