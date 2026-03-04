from fastapi import FastAPI
from app.database import Base, engine
from app.routes import users as user_route
from app.routes import categories as category_route
from app.routes import accounts as account_route
from app.routes import transactions as transaction_route
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

app.include_router(user_route.router)
app.include_router(account_route.router)
app.include_router(category_route.router)
app.include_router(transaction_route.router)