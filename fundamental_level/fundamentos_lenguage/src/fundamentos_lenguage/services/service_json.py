import json
import re
from typing import cast

import aiofiles

from ..constants.constants import GENDER_SWAP, LATIN_ALFABET


async def main():
    data = await read_json_async(
        "/Users/MX-YADAESVE-MACM4/Desktop/curso_python/fundamental_level/fundamentos_lenguage/src/fundamentos_lenguage/models/data.json"
    )
    await read_json_async(
        "/Users/MX-YADAESVE-MACM4/Desktop/curso_python/fundamental_level/fundamentos_lenguage/src/fundamentos_lenguage/models/data_error.json"
    )
    await read_json_async(
        "/Users/MX-YADAESVE-MACM4/Desktop/curso_python/fundamental_level/fundamentos_lenguage/src/fundamentos_lenguage/models/data_non-exist.json"
    )
    if data:
        results: list[dict] = cast(list[dict], data["results"])
        get_max_age(results)
        separate_per_gender(results)
        filter_by_latin_name(results)


async def read_json_async(path) -> dict[str, list[dict] | object] | None:
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


def separate_per_gender(results):
    male_list = []
    female_list = []

    for person in results:
        gender = person.get("gender")
        genero = GENDER_SWAP.get(gender, "desconocido")
        name = get_name(person)
        if person["gender"] == "male":
            male_list.append(f"{name} es {genero}")
        elif person["gender"] == "female":
            female_list.append(f"{name} es {genero}")

    print("this is the male list")
    print(male_list)
    print("this is the female list")
    print(female_list)
    print("\n")


def get_max_age(results: list[dict]) -> None:
    max_age: int = 0
    output_list: list = []
    while True:
        user_input = input("Ingresa la edad maxima para filtrar > ")

        try:
            max_age = int(user_input)
            break
        except ValueError:
            print("Favor de ingresar un numero")

    for person in results:
        dob: dict = person.get("dob") or {}
        age: int = dob.get("age") or 0
        name: str = get_name(person)
        if age < max_age:
            output_list.append(f"{name} tiene menos de {max_age} tiene {age} años")
    if not output_list:
        print(f"Nadie tiene menos de {max_age} años")
    else:
        for output in output_list:
            print(output)
        print(f"personas con menos de {max_age} son {len(output_list)}")
    print("\n")


def filter_by_latin_name(results) -> None:
    for person in results:
        name = get_name(person)
        match name:
            case n if re.search(LATIN_ALFABET, n):
                print(f"{n} contiene caracteres fuera del alfabeto latino")
            case n:
                print(f"{n} es un nombre latino")
    print("\n")


def get_name(person) -> str:
    firstName = person.get("name").get("first")
    lastName = person.get("name").get("last")
    return f"{firstName} {lastName}"
