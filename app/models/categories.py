from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum
from app.database import Base

class TransactionType(enum.Enum):
    EXPENSE = "expense"
    INCOME = "income"

class Name(enum.Enum):
    FOOD = "food"
    RENT = "rent"
    SALARY = "salary"
    TRANPORT = "transport"
    CLOTHES = "clothes"
    OTHER  = "other"

class Categories(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(Enum(Name))
    trans_type = Column(Enum(TransactionType), nullable=False)

    transactions = relationship("Transactions", back_populates="categories")
    user = relationship("Users", back_populates="categories")