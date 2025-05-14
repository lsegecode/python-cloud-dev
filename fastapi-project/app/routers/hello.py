from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "¡Hola desde FastAPI, Lucas!"}

@router.get("/ping")
def ping():
    return {"ping": "pong"}
