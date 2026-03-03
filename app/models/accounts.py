from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Numeric, Enum
import enum
from sqlalchemy.dialects.postgresql import ENUM as PG_ENUM
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class AccountName(enum.Enum):
    CASH = "CASH"
    BANK = "BANK"
    CREDIT_CARD = "CREDIT_CARD"
    CRYPTO_CURRENCY = "CRYPTO_CURRENCY"


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(PG_ENUM(AccountName, name="account_name_enum", create_type=True), nullable=False)
    balance = Column(Numeric(10,2), default=0, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates= "accounts")
    transactions = relationship("Transaction", back_populates="account", cascade="all, delete-orphan")
