from fastapi import APIRouter

router = APIRouter()

@router.get("/user")
def read_root():
    return {"message": "¡Hola desde FastAPI, Lucas!"}

@router.get("/ping2")
def ping():
    return {"a": "pong"}
