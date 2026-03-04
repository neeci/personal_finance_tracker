from pydantic import BaseModel
from datetime import datetime

class TransactionResponse(BaseModel):
    amount:int
    description:str|None
    created_at:datetime
