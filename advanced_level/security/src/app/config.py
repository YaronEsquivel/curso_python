# src/app/config.py

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str
    debug: bool = False

    class Config:
        env_file = ".env"
