from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.core.auth import get_current_active_user
from app.schemas.users import User
from app.crud.transactions import create_, get_, delete_
from app.schemas.transactions import TransactionResponse, TransactionDetail

router = APIRouter (
    prefix = '/transaction',
    tags = ['Transactions']
)

@router.post('/create', response_model=TransactionResponse)
async def create(account_id:int, category_id:int, 
    amount: int, description:str=None, db:Session=Depends(get_db), 
    user:User = Depends(get_current_active_user)):
    return create_(user_id=user.id, account_id=account_id, 
    category_id=category_id, amount=amount, description=description, db=db)

@router.get('/list', response_model=list[TransactionDetail])
async def get(db:Session=Depends(get_db), 
    user:User=Depends(get_current_active_user)):
    return get_(db=db, user_id=user.id)

@router.delete('/delete')
async def delete(id:int, db:Session= Depends(get_db), user:
    User = Depends(get_current_active_user)):
    return delete_(db, id)