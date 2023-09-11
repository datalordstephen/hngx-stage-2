from sqlalchemy import Column, Integer, String
from database import Base

# create table as a class
class Person(Base):
    __tablename__ = 'persons'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False, index=True)