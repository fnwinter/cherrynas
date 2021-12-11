from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

Base = declarative_base()

class Account(Base):
    __tablename__ = 'account'
    email = Column(String, primary_key=True, nullable=False)
    password = Column(String, nullable=False)
    reset_pin = Column(String(6))
