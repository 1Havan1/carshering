from app import Base
from sqlalchemy import Column, Integer, String, Float

class Car(Base):
    __tablename__ = 'Cars'
    id = Column(Integer, primary_key=True)
    sign = Column(String, unique = True)
    mark = Column(String)
    price_at_minute = Column(Float)