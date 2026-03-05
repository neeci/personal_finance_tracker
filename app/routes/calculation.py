from fastapi import APIRouter, Depends
from app.database import get_db
from app.core.auth import get_current_active_user
from app.schemas.users import User
from sqlalchemy.orm import Session
from app.models.transactions import Transaction
from sqlalchemy import func, case
from app.models.transactions import Transaction
from app.models.categories import Category

router = APIRouter(
    prefix = "/calculate",
    tags = ["Calculate"]
)
def calculate_(db:Session, id:int):
    variable = db.query(Transaction).filter(user_id == id).all()
    


@router.get('/total')
async def calculate(user:User=Depends(get_current_active_user),
    db:Session= Depends(get_db)):
    balance = (
    db.query(
        func.sum(
            case(
                (Category.trans_type == "INCOME", Transaction.amount),
                else_=-Transaction.amount
            )
        ).label("balance")
    )
    .join(Category)
    .scalar()
)
    return {"message" : f"Total balance is ${balance}"}