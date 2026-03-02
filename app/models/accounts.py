from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship

from app.database import Base



class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String, nullable=False)
    balance = Column(Numeric(10,2), default=0, nullable=False)
    created_at = Column(DateTime)

    user = relationship("User", back_populates= "accounts")
    transactions = relationship("Transaction", back_populates="account", cascade="all, delete-orphan")
