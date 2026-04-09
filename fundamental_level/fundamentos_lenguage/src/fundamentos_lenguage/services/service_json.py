import json

import aiofiles


async def main():
    data = await read_json_async(
        "/Users/MX-YADAESVE-MACM4/Desktop/curso_python/fundamental_level/fundamentos_lenguage/src/fundamentos_lenguage/models/data.json"
    )
    print(data)


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
