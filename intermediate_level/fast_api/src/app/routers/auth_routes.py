from app.core.security import create_access_token
from fastapi import APIRouter

router = APIRouter()


@router.post("/get_token")
def login():
    user_data = {"id": 1, "sub": "test@email.com"}

    token = create_access_token(user_data)

    return {"access_token": token, "token_type": "bearer"}
