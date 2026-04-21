from app.infraestructure import models  # noqa: F401
from app.infraestructure.db.session import engine
from app.infraestructure.models.base import Base


def init_db():
    Base.metadata.create_all(bind=engine)
