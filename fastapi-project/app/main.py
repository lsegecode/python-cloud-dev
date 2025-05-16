from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.models.user import Base
from app.database import engine
from app.routers import hello, user

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    Base.metadata.create_all(bind=engine)
    yield
    # Shutdown code (optional cleanup)

app = FastAPI(lifespan=lifespan)

app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(hello.router, tags=["Hello"])
