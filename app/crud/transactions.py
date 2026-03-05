from sqlalchemy.orm import Session
from datetime import datetime
from app.models.transactions import Transaction


def create_(user_id:int, account_id:int, category_id:int, amount:int,
    db:Session, description:str=None):
    transaction = Transaction(user_id=user_id, account_id=account_id, 
    category_id=category_id, amount=amount, description=description,
    created_at=datetime.utcnow())
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction

def get_(user_id:int, db:Session):
    return db.query(Transaction).filter(user_id==user_id).all()

def delete_(db:Session, id:int):
    parameter = db.query(Transaction).filter(Transaction.id==id).first() 
    db.delete(parameter)
    db.commit()
    return {
        "message" : "Transaction deleted successfully"
    }
    
