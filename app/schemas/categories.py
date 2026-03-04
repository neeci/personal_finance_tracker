from enum import Enum
import enum
from pydantic import BaseModel

class TransTypeEnum(str, Enum):
    EXPENSE = "EXPENSE"
    INCOME = "INCOME"

class TransNameEnum(str, Enum):
    FOOD = "FOOD"
    RENT = "RENT"
    SALARY = "SALARY"
    TRANSPORT = "TRANSPORT"
    CLOTHES = "CLOTHES"
    OTHER  = "OTHER"

class CategoryResponse(BaseModel):
    id:int
    transaction_name: str
    trans_type:str