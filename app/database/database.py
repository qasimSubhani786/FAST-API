from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import settings

# Database URL from environment variables
DATABASE_URL = settings.DATABASE_URL

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a configured SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()