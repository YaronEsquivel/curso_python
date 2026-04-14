from app.models import Item, Order, OrderItem, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def seed_data():
    session = SessionLocal()

    # usuario
    user = User(name="Juan", email="juan@mail.com")
    session.add(user)

    # item
    item = Item(name="Laptop", price=1000)
    session.add(item)

    session.commit()

    # orden
    order = Order(user_id=user.id)
    session.add(order)
    session.commit()

    # order item
    order_item = OrderItem(order_id=order.id, item_id=item.id, quantity=2)
    session.add(order_item)
    session.commit()

    print("Datos insertados correctamente")
