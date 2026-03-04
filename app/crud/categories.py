from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.categories import TransNameEnum, TransTypeEnum
from app.models.categories import Category

def create_(db:Session, user_id:int, 
    trans_name: TransNameEnum, trans_type:TransTypeEnum):
    catVariable = Category(user_id=user_id, transaction_name=trans_name,
    trans_type=trans_type)
    db.add(catVariable)
    db.commit()
    db.refresh(catVariable)
    return catVariable

def get_categories_(db:Session, user_id:int):
    return db.query(Category).filter(user_id == user_id).all()
