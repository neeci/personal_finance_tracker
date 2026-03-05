from pydantic import BaseModel
from datetime import datetime
from app.schemas.categories import CategoryResponse

class TransactionResponse(BaseModel):
    id:int
    amount:int
    description:str|None
    created_at:datetime

class TransactionDetail(BaseModel):
    id:int
    amount:int
    category: CategoryResponse
    description:str|None
    created_at:datetime 
