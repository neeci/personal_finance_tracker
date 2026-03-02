from fastapi import FastAPI
from app.database import Base, engine
from app.routes import users as newuser
from app.models import accounts, categories, transactions, users


Base.metadata.create_all(engine)

app = FastAPI()

from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    print("Validation error:", exc.errors())
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()},
    )
    
app.include_router(newuser.router)