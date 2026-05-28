from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# This line creates the database file at golf.db
DATABASE_URL = "sqlite:///./golf.db"

# This creates a connection to the database
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

# This creates a session factory - think of it like a connection pool
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# This is the base class all our data models inherit from
Base = declarative_base()

# This function gives each API request its own database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()