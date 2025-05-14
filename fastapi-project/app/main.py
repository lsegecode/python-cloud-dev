from fastapi import FastAPI
from app.routers import hello, user

app = FastAPI()

app.include_router(hello.router)
app.include_router(user.router)
