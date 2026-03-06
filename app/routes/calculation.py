from fastapi import APIRouter, Depends
from app.database import get_db
from app.core.auth import get_current_active_user
from app.schemas.users import User
from sqlalchemy.orm import Session
from app.models.transactions import Transaction
from sqlalchemy import func, case, and_
from app.models.transactions import Transaction
from app.models.categories import Category
from datetime import datetime, timedelta

router = APIRouter(
    prefix = "/calculate",
    tags = ["Calculate"]
)
    
time_filter = datetime.utcnow() - timedelta(minutes = 30)

@router.get('/monthly/total')
async def total(user:User=Depends(get_current_active_user),
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
    .filter(Transaction.created_at >= time_filter)
    .join(Category)
    .scalar()
    )
    return {"message" : f"Total balance is ${balance}"}

@router.get('/total')
async def total(user:User=Depends(get_current_active_user),
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

@router.get('/monthly/income')
async def total_income(user:User = Depends(get_current_active_user),
    db:Session = Depends(get_db)):
    income = (
        db.query(
            func.sum(
                case(
                    (Category.trans_type == "INCOME", Transaction.amount),
                    else_ = 0
                )   
            ).label("total_income")
        ).filter(Transaction.created_at >= time_filter)
        .join(Category)
        .scalar()
        )
    return {"message": f"Your total income for this month is ${income}"}

@router.get('/income')
async def total_income(user:User = Depends(get_current_active_user),
    db:Session = Depends(get_db)):
    income = (
        db.query(
            func.sum(
                case(
                    (Category.trans_type == "INCOME", Transaction.amount),
                    else_ = 0
                )   
            ).label("total_income")
        ).join(Category)
        .scalar()
        )
    return {"message": f"Your total income for this month is ${income}"}

@router.get('/monthly/expense')
async def total_expenses(db:Session = Depends(get_db),
    user:User = Depends(get_current_active_user)):
    expenses = (
        db.query(
            func.sum(
                case(
                    (Category.trans_type == "EXPENSE", Transaction.amount),
                    else_ = 0
                )
            ).label("expenses")
        )
        .filter(Transaction.created_at >= time_filter)
        .join(Category)
        .scalar()
    )
    return {"message":f"Your total expense for this month was ${expenses}"}

@router.get('/expense')
async def total_expenses(db:Session = Depends(get_db),
    user:User = Depends(get_current_active_user)):
    expenses = (
        db.query(
            func.sum(
                case(
                    (Category.trans_type == "EXPENSE", Transaction.amount),
                    else_ = 0
                )
            ).label("expenses")
        )
        .join(Category)
        .scalar()
    )
    return {"message":f"Your total expense for this month was ${expenses}"}

@router.get('/category')
async def category(db:Session = Depends(get_db),
    user:User = Depends(get_current_active_user)):
    categories = ["FOOD", "RENT", "SALARY", "TRANSPORT", "CLOTHES", "OTHER"]
    totals = {}
    for cat in categories:
        row = db.query(
            func.sum(
                case(
                    (and_(Category.transaction_name == cat,
                        Category.trans_type == "INCOME"),
                    Transaction.amount),
                    else_=0
                )
            ).label("income"),
            func.sum(
                case(
                    (and_(Category.transaction_name == cat,
                        Category.trans_type == "EXPENSE"),
                    Transaction.amount),
                    else_=0
                )
            ).label("expense")
        ).join(Category).first()

        income = row.income or 0
        expense = row.expense or 0

        totals[cat] = {
            "income": income,
            "expense": expense,
            "net": income-expense
        }
    return totals



