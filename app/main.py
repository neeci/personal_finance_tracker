from fastapi import FastAPI
from app.database import Base, engine
from app.routes import users


Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(users.router)