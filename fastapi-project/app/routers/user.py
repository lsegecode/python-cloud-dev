from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserRead
from app.models.user import User
from app.dependencies import get_db

router = APIRouter()


@router.get(
        "/{user_id}", 
        response_model=UserRead, 
        summary="Get user by ID", 
        description="Retrieve a user from the database by their unique ID.")
def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Get a user by ID.

    - **user_id**: The unique ID of the user to retrieve.
    - Returns the user data if found, otherwise returns a 404 error.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")


@router.post(
        "/", 
        response_model=UserRead, 
        summary="Create a new user", 
        description="Create a new user with name and email. Returns the created user data.")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user.

    - **user**: A JSON object with user `name` and `email`.
    - Returns the created user with generated ID.
    """
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
