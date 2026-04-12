import csv
import logging
from datetime import datetime
from pathlib import Path
from typing import Callable

from ..clases.Order import Order
from ..model.OrderIn import OrderIn
from ..model.outputModel import OutputModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def main():
    INPUT_PATH: Path = Path(__file__).parent.parent / "input" / "order.csv"
    OUTPUT_PATH: Path = Path(__file__).parent.parent / "output" / "output.json"
    ordersIn = load_from_csv(INPUT_PATH)
    logger.info(f" Se encontraron {len(ordersIn)} registros")
    orders = map_to_orderIn_to_order(ordersIn)
    output: OutputModel = OutputModel()
    output.metrics = calculate_metrics(orders)
    output.by_status = calculate_by_status(orders)
    output.top_users = calculate_top_users(orders)
    write_in_json(output, OUTPUT_PATH)


def load_from_csv(path: Path) -> list[OrderIn]:
    with path.open() as file:
        logger.info(" Leyendo datos del csv")
        reader = csv.DictReader(file)
        return [
            OrderIn(
                order_id=row["order_id"],
                user_id=row["user_id"],
                amount=row["amount"],
                status=row["status"],
                created_at=row["created_at"],
            )
            for row in reader
        ]


def map_to_orderIn_to_order(ordersIn: list[OrderIn]) -> list[Order]:
    orders: list[Order] = []
    for orderIn in ordersIn:
        try:
            if orderIn.status not in ("completed", "failed", "pending"):
                raise ValueError(f" '{orderIn.status}' estatus desconocido ")
            order: Order = Order(
                int(orderIn.order_id),
                int(orderIn.user_id),
                float(orderIn.amount),
                orderIn.status,
                datetime.strptime(orderIn.created_at, "%Y-%m-%d"),
            )
            orders.append(order)
        except ValueError as e:
            logger.warning(f" {e.args[0]} en la orden no. {orderIn.order_id}")
    return orders


def filter_per_status(status: str) -> Callable[[list[Order]], list[Order]]:
    def filter(orders: list[Order]) -> list[Order]:
        return [order for order in orders if status == order.status]

    return filter


def calculate_metrics(orders):
    total_orders = len(orders)
    total_revenue = sum(order.amount for order in orders)
    avg_order_value = round(total_revenue / total_orders, 2)

    return {
        "total_orders": total_orders,
        "total_revenue": total_revenue,
        "avg_order_value": avg_order_value,
    }


def calculate_by_status(orders: list[Order]):
    complete_filter = filter_per_status("completed")
    failed_filter = filter_per_status("failed")
    pending_filter = filter_per_status("pending")

    completed = {"completed": len(complete_filter(orders))}
    failed = {"failed": len(failed_filter(orders))}
    pending = {"pending": len(pending_filter(orders))}

    return {**completed, **failed, **pending}


def calculate_top_users(orders: list[Order]):
    top_users = sorted(orders, key=lambda o: o.amount, reverse=True)[:3]
    return [
        {"id_orden": top.order_id, "id_usuario": top.user_id, "cantidad": top.amount}
        for top in top_users
    ]


def write_in_json(output: OutputModel, path: Path):
    path.write_text(output.model_dump_json())
