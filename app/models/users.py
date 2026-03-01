from app.database import Base
from sqlalchemy import Column, String, Integer, Boolean, DateTime
from sqlalchemy.orm import relationship

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean)
    created_at = Column(DateTime)

    accounts =relationship("Accounts", back_populates="user")
    categories = relationship("Categories", back_populates ="user")
    transactions = relationship("Transactions", back_populates="user")

