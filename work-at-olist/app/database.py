from sqlalchemy import create_engine
from sqlalchemy  import declarative_base,sessionmaker

ENGINE = create_engine('sqlite:///database_authors.db')

Base = declarative_base()
Session = sessionmaker(bind=ENGINE)
session = Session()

