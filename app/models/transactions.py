from sqlalchemy import Column, String, Integer, ForeignKey, Enum, DateTime, Numeric
from sqlalchemy.orm import relationship
import enum
from datetime import datetime
from app.database import Base

class Transaction(Base):
    __tablename__="transactions"

    id = Column(Integer, primary_key=True)
    
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), index=True)
    account_id = Column(Integer, ForeignKey("accounts.id", ondelete="CASCADE"), index=True)
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), index=True)
    
    amount = Column(Numeric(10, 2), nullable=False)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="transactions")
    account = relationship("Account", back_populates="transactions")
    category = relationship("Category", back_populates="transactions")