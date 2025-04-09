from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

import os
from dotenv import load_dotenv

# Load environment variables from ..env file
load_dotenv()

DB_USER = os.getenv("PY_DB_USER")
DB_PASSWORD = os.getenv("PY_DB_PASSWORD")
DB_HOST = os.getenv("PY_DB_HOST")
DB_PORT = os.getenv("PY_DB_PORT")
DB_NAME = os.getenv("PY_DB_NAME")

# Construct the DATABASE_URL
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(
    DATABASE_URL,
    pool_size=20,  # The size of the pool to be maintained
    max_overflow=10,  # The maximum overflow size
    pool_timeout=30,  # Timeout for getting a connection from the pool
    pool_recycle=1800,  # Recycle connections after this many seconds
)

SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()