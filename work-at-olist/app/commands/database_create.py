from sqlalchemy import create_engine,Column,Integer,String, insert
from sqlalchemy.orm import declarative_base, sessionmaker
import numpy as np

engine = create_engine('sqlite:///database_authors.db')

#Defining the base to the columns
Base = declarative_base()

#Creating what represents the table
class Author(Base):
    __tablename__ = "authors" # Defining the name of the table

    id = Column(Integer,primary_key=True)
    name = Column(String(90))
   
        
def create_table():
    Base.metadata.create_all(engine) #Creating the table

    Session = sessionmaker(bind=engine)
    global session 
    session = Session()

    #Saving the alteration (commit)
    session.commit()

def insert_author_name(name):
        
    #Inserting data
    try:
        new_user = Author(name=name)
        session.add(new_user)
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
create_table()


