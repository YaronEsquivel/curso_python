from pydantic import BaseModel


class UserCreate(BaseModel):
    nombre: str
    correo: str


class UserResponse(UserCreate):
    id: int

    class Config:
        from_attributes = True
