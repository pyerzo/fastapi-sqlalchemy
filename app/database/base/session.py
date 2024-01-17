"""Database configuration"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.utils.tools import env

TYPE = "postgresql"
USER: str = env("POSTGRES_USER")
PASSWORD: str = env("POSTGRES_PASSWORD")
HOST: str = env("POSTGRES_HOST")
PORT: str = env("POSTGRES_PORT")
DATABASE: str = env("POSTGRES_DB")

url = f"{TYPE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

engine = create_engine(url, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
metadata = Base.metadata


def get_session():
    """Returns database session"""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
