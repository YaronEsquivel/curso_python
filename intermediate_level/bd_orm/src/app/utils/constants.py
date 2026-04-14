from app.models import Item, Order, User

TABLE_ACTIONS = {1: (User, "Usuario"), 2: (Order, "Orden"), 3: (Item, "Item")}

SKIP_FIELDS = {"id", "created_at", "_sa_instance_state", "order_id"}
