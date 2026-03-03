from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class Account(BaseModel):
    id:int
    user_id:int
    name:str
    balance:int
    created_at:datetime

class AccountResponse(BaseModel):
    id:int
    name:str
    balance:int
    created_at: datetime

class AccountNameEnum(str, Enum):
    CASH = "CASH"
    BANK = "BANK"
    CREDIT_CARD = "CREDIT_CARD"
    CRYPTO_CURRENCY = "CRYPTO_CURRENCY"

