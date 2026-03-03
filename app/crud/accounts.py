from app.database import get_db
from datetime import datetime
from app.models.accounts import Account
from sqlalchemy.orm import Session
from app.schemas.accounts import AccountNameEnum

def create(db:Session, user_id:int, name:AccountNameEnum, balance:int, created_at:datetime):
    account = Account(user_id=user_id, name=name, balance=balance,
    created_at=datetime.utcnow())
    db.add(account)
    db.commit()
    db.refresh(account)
    return account

def accounts(db:Session, user_id):
    accounts = db.query(Account).filter(Account.user_id == user_id).all()
    return accounts