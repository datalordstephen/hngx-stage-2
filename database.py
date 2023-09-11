from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL = "postgresql://emmqlwji:LYbQF__5WQYGlfyN7GT89QtQW8vQxheD@mel.db.elephantsql.com/emmqlwji"

engine = create_engine(URL)
SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)

Base = declarative_base()