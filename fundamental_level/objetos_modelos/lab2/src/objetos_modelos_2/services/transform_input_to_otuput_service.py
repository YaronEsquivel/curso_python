import json
from typing import Any

import aiofiles

from ..clases.Order import Order
from ..models.OrderIn import OrderIn
from ..models.OrderOut import OrderOut


async def main():
    data = await read_json_async(
        "/Users/MX-YADAESVE-MACM4/Desktop/curso_python/fundamental_level/objetos_modelos/lab2/src/objetos_modelos_2/utils/data.json"
    )
    ordersIn: list[OrderIn] = []
    if data:
        for orderDTO in data:
            try:
                order = OrderIn(**orderDTO)
                ordersIn.append(order)
            except Exception as e:
                print(f"Hubo un error en la orden {orderDTO}")
                print(e)
                print("\n")
        orders = transform_to_order(ordersIn)
        ordersOut = transform_to_out(orders)
        show_orders(ordersOut)


async def read_json_async(path: str) -> list[dict[str, Any]] | None:
    try:
        async with aiofiles.open(path, mode="r", encoding="utf-8") as f:
            content = await f.read()
            data = json.loads(content)
    except FileNotFoundError:
        print("El archivo no existe.")
        return None
    except json.JSONDecodeError:
        print("JSON inválido.")
        return None
    else:
        return data


def show_orders(orders: list[OrderOut]) -> None:
    for order in orders:
        print(order)


def transform_to_order(ordersIn: list[OrderIn]) -> list[Order]:
    orders: list[Order] = []
    for index, orderDTO in enumerate(ordersIn):
        order = Order(id=index + 1, **orderDTO.dict())
        orders.append(order)
    return orders


def transform_to_out(orders: list[Order]) -> list[OrderOut]:
    ordersOut: list[OrderOut] = []
    for order in orders:
        orderOut = OrderOut(
            id=order.id,
            producto=order.product,
            cantidad=order.quantity,
            precio_unitario=order.unit_price,
            total=order.total,
        )
        ordersOut.append(orderOut)
    return ordersOut
