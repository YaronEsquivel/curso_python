from app.infraestructure.security.security import create_access_token
from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post(
    "/get_token",
    summary="obtener token de autenticación",
    description="Genera un token de autenticación para counicarse con los demás endpoints",
)
def login():
    user_data = {"id": 1, "sub": "test@email.com"}

    token = create_access_token(user_data)

    return {"access_token": token, "token_type": "bearer"}
