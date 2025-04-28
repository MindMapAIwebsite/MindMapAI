from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import redis
from .config import settings

# PostgreSQL connection
engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Redis connection
redis_client = redis.from_url(settings.REDIS_URL)

def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_redis():
    """Get Redis client"""
    return redis_client

def init_db():
    """Initialize database"""
    Base.metadata.create_all(bind=engine)

def close_db_connection():
    """Close database connection"""
    engine.dispose() 