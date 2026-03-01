from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base

database = "postgresql://nissi:nissikwasu@localhost:5432/finances"
engine = create_engine(database, echo=True)
Base = declarative_base()

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()
        