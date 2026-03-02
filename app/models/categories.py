from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum
from app.database import Base

class TransactionType(enum.Enum):
    EXPENSE = "expense"
    INCOME = "income"

class trans_name(enum.Enum):
    FOOD = "food"
    RENT = "rent"
    SALARY = "salary"
    TRANPORT = "transport"
    CLOTHES = "clothes"
    OTHER  = "other"

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), index=True)
    transaction_name = Column(Enum(trans_name), nullable=False)
    trans_type = Column(Enum(TransactionType), nullable=False)

    transactions = relationship("Transaction", back_populates="category", cascade="all, delete-orphan")
    user = relationship("User", back_populates="categories")