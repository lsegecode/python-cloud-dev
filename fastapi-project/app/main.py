from fastapi import FastAPI
from app.routers import hello, user
from app.models.user import Base
from app.database import engine

app = FastAPI()

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(hello.router, tags=["Hello"])


