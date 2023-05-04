from app import Base
from sqlalchemy import Column, Integer, String, Float

class User(Base):
    __tablename__='users'
    username = Column(String)
    password_hash = Column(String)