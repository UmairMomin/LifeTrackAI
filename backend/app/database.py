from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Database URL from .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Create engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()


# Dependency for DB session (used in routes/services)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create tables in the database (auto-run in dev mode from main.py)
def create_tables():
    from app.models import user, task, ai_insight
    Base.metadata.create_all(bind=engine)
