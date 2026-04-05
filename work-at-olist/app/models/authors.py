from sqlalchemy import Column,Integer,String
from app.database import Base

#Creating what represents the table
class Author(Base):
    __tablename__ = "authors" # Defining the name of the table

    id = Column(Integer,primary_key=True)
    name = Column(String(90))
   