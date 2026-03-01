from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base



class Accounts(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", 
                ondelete="CASCADE"), nullable=False)
    name = Column(String)
    balance = Column(Integer)
    created_at = Column(DateTime)

    user = relationship("Users", back_populates= "accounts")
    transactions = relationship("Transactions", back_populates="accounts")
