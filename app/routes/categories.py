from fastapi import APIRouter, Depends
from app.crud.categories import create_, get_categories_
from app.schemas.categories import TransNameEnum, TransTypeEnum
from app.core.auth import get_current_active_user
from app.schemas.users import User
from app.database import get_db
from sqlalchemy.orm import Session
from app.schemas.categories import CategoryResponse

router = APIRouter (
    prefix = '/category',
    tags = ['Category']
)

@router.post('/create', response_model=CategoryResponse)
async def create(trans_name:TransNameEnum, trans_type:TransTypeEnum,
    user:User = Depends(get_current_active_user), db:Session=Depends(get_db)):
    return create_(user_id=user.id, trans_name=trans_name, 
    trans_type=trans_type, db=db)

@router.get('/list', response_model=list[CategoryResponse])
async def get_categories(db:Session = Depends(get_db), 
    user:User = Depends(get_current_active_user)):
    return get_categories_(db=db, user_id=user.id)