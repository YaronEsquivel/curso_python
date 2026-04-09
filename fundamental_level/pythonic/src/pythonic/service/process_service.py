import json
import re

import aiofiles

from ..service.timer import Timer
from ..utils.constants import NAME_PATTERN
from ..utils.decorators import count_pokemons, retry


async def main():
    with Timer():
        data = await read_json_async(
            "/Users/MX-YADAESVE-MACM4/Desktop/curso_python/fundamental_level/pythonic/src/pythonic/utils/data.json"
        )
        pokemons = data.get("results")
        process_info(pokemons)


async def read_json_async(path):
    try:
        async with aiofiles.open(path, mode="r", encoding="utf-8") as f:
            content = await f.read()
            data = json.loads(content)
    except FileNotFoundError:
        print("El archivo no existe.")
    except json.JSONDecodeError:
        print("JSON inválido.")
    else:
        return data


def process_info(pokemons):
    for pokemon in pokemons:
        capitalized_name = (lambda name: name.capitalize())(pokemon.get("name"))
        if re.search(NAME_PATTERN, capitalized_name):
            print(f"El nombre de {capitalized_name} tiene carecteres extraños")
            corrected_name = re.sub(NAME_PATTERN, "", capitalized_name)
            print(f"Nombre corregido: {corrected_name}")
            pokemon["name"] = corrected_name
        else:
            print(f"{capitalized_name}")
            pokemon["name"] = capitalized_name
    print("**************** \n")

    filter_poison = filter_per_type("poison")
    filter_normal = filter_per_type("normal")
    filter_bug = filter_per_type("bug")

    poison_pokemons = filter_poison(pokemons=pokemons)
    print("pokemons tipo veneno")
    print(poison_pokemons)
    print("**************** \n")
    normal_pokemons = filter_normal(pokemons=pokemons)
    print("pokemons tipo normal")
    print(normal_pokemons)
    print("**************** \n")
    bug_pokemons = filter_bug(pokemons=pokemons)
    print("pokemons tipo bicho")
    print(bug_pokemons)
    print("**************** \n")

    filter_per_max_id(pokemons)
    print("**************** \n")

    pokemon_lists = generate_lists(pokemons, size=5)
    print(next(pokemon_lists))
    print("**************** \n")
    print(next(pokemon_lists))


def filter_per_type(type):
    def filter(pokemons):
        return [p for p in pokemons if type in p["types"]]

    return filter


@retry(max_retry_attempts=5, backoff_factor=1, exceptions=(ValueError,))
@count_pokemons
def filter_per_max_id(pokemons):
    output = []
    while True:
        user_value = input("Agrega un id maximo para buscar > ")
        try:
            max_id = int(user_value)
            break
        except ValueError:
            raise ValueError("Favor de ingresar un numero")
    for p in pokemons:
        try:
            id = int(p["id"])
            if id <= max_id:
                output.append(p)
        except ValueError:
            print(f"El id {p['id']} esta eroneo")
            p["id"] = re.findall(r"\d+", p["id"])[0]

    return output


def generate_lists(pokemons, size):
    output = []
    for pokemon in pokemons:
        output.append(pokemon)
        if len(output) == size:
            yield output
            output = []
    if output:
        yield output
