from pydantic import BaseModel, EmailStr, Field


class UserRequest(BaseModel):
    nombre: str = Field(min_length=3, max_length=50)
    correo: EmailStr

    class Config:
        from_attributes = True
