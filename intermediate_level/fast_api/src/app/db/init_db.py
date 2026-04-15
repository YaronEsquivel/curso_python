from app import models  # noqa: F401
from app.db.session import engine
from app.models.Base import Base


def init_db():
    Base.metadata.create_all(bind=engine)
