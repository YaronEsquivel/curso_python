import logging

from app.config.db import SessionLocal
from app.models import Order, OrderItem, User
from app.utils.constants import SKIP_FIELDS, TABLE_ACTIONS

logger = logging.getLogger(__name__)
session = SessionLocal()


def query_data():
    users = session.query(User).all()
    return users


def menu():
    option = 0
    while option != 5:
        print("Selecciona una opción: ")
        print("1.- Consultar tabla de la base de datos")
        print("2.- Agregar registro a la base de datos")
        print("3.- Eliminar registro de la base de datos")
        print("4.- Actualizar registro de la base de datos")
        print("5.- Salir")
        option = input(" > ")
        try:
            option = int(option)
        except ValueError:
            logger.error("No se ingreso una opción valida")
        if option != 5:
            handle_action(option)


def handle_action(option):
    table = 0
    print("Selecciona una tabla: ")
    print("1.- Users")
    print("2.- Orders")
    print("3.- Items")
    print("4.- volver")
    table = input(" > ")
    try:
        table = int(table)
    except ValueError:
        logger.error("No se ingreso una opción valida")
    if table < 4:
        selected_action_and_table(option, table)
    if table > 4:
        logger.error("No se ingreso una opción valida")


def selected_action_and_table(option, table):
    info = TABLE_ACTIONS.get(table)
    if info:
        model, label = info
    if option == 1:
        list_records(model, label)
    if option == 2:
        create_record(model, label)
    if option == 3:
        print(f"Ingresa el id del {label} a eliminar")
        id_input = input(" > ")
        try:
            id_input = int(id_input)
            delete_record(model, id_input)
        except ValueError:
            logger.error("Se recibio una respuesta invalida")
    if option == 4:
        print(f"Ingresa el id del {label} a actualizar")
        id_input = input(" > ")
        try:
            id_input = int(id_input)
            update_record(model, id_input)
        except ValueError:
            logger.error("Se recibio una respuesta invalida")


def list_records(model, label):
    records = session.query(model).all()
    if not records:
        print(f"No existen registros en la tabla {model}")
    print("\n")
    for r in records:
        print(f"{label}: {r}")
        if model == Order:
            for oi in r.items:
                print(
                    f"items: {oi.item.name}, cantidad: {oi.quantity}, costo total: {int(oi.quantity) * int(oi.item.price)}"
                )
    print("\n")


def create_record(model, label):
    fields = {}

    for column in model.__table__.columns:
        if column.name in SKIP_FIELDS:
            continue
        value = input(f"{column}: ")
        fields[column.name] = value

    record = model(**fields)
    session.add(record)

    if model == Order:
        fields_name = {}
        item_id = input("item_id: ")
        quantity = input("quantity: ")
        fields_name = {"item_id": item_id, "quantity": quantity}
        record_info = OrderItem(**fields_name)
        record.items.append(record_info)

    session.commit()

    print(f"Se creo el {label} {record}")


def delete_record(model, id_input):
    record = session.query(model).filter_by(id=id_input).first()
    if not record:
        logger.warning("No existe el id seleccionado")
    session.delete(record)
    session.commit()
    print(f"se elimino: {record}")


def update_record(model, id_input):
    record = session.query(model).filter_by(id=id_input).first()
    for key, value in record.__dict__.items():
        if key in SKIP_FIELDS:
            continue
        print(f"{key} antiguo valor {value}")
        input_value = input("Ingresa nuevo valor > ")
        setattr(record, key, input_value)
    if model == Order:
        orderItems = record.items
        for orderItem in orderItems:
            for key_oi, value_oi in orderItem.__dict__.items():
                if key_oi in SKIP_FIELDS:
                    continue
                print(f"order item: {key_oi} : {value_oi}")
                input_oi_value = input("Ingresar nuevo valor > ")
                setattr(orderItem, key_oi, input_oi_value)
    session.commit()
    logger.info(f"Información de {model} actualizada")
