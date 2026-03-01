from sqlalchemy import Column, String, Integer, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
import enum
from app.database import Base

class Transaction(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    account_id = Column(Integer, ForeignKey("accounts.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    amount = Column(Integer)
    transaction_type = Column(Enum, ForeignKey("categories.trans_type")) 
    description = Column(String)
    

    user = relationship("Users", back_populates="transactions")
    accounts = relationship("Users", back_populates="transactions")
    categories = relationship("Users", back_populates="transactions")