from sqlalchemy import create_engine,Column,Integer,String, insert
from sqlalchemy.orm import declarative_base, sessionmaker
import numpy as np
from colorama import Fore
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

def insert_author_name(batch_name):
        
    #Inserting data
    try:
        for item in batch_name:
            name = str(item [0]).strip(("[]''")) if item else ""
            session.add(Author(name = name))
        session.commit()
    except Exception as e:
        print(Fore.RED+f"ERROR: {e.__cause__}")
        session.rollback()
        raise
    finally:
        session.close()

create_table()


