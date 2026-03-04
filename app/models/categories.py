from sqlalchemy import Column, String, Integer, ForeignKey, Enum, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ENUM as PG_ENUM
import enum
from app.database import Base

class TransactionType(enum.Enum):
    EXPENSE = "EXPENSE"
    INCOME = "INCOME"

class Trans_Name(enum.Enum):
    FOOD = "FOOD"
    RENT = "RENT"
    SALARY = "SALARY"
    TRANSPORT = "TRANSPORT"
    CLOTHES = "CLOTHES"
    OTHER  = "OTHER"

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), index=True)
    transaction_name = Column(PG_ENUM(Trans_Name, name="TransNameEnum", create_type=True), nullable=False)
    trans_type = Column(PG_ENUM(TransactionType, name="TransTypeEnum", create_type=True), nullable=False)

    transactions = relationship("Transaction", back_populates="category", cascade="all, delete-orphan")
    user = relationship("User", back_populates="categories")