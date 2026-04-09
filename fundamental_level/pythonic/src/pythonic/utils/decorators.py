import time


def count_pokemons(func):
    def decorador(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print(f"se encontraron {len(resultado)} pokemons")
        print(f"{[{p['name'], p['id']} for p in resultado]}")
        return resultado

    return decorador


def retry(max_retry_attempts=3, backoff_factor=1, exceptions=(Exception,)):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < max_retry_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempt += 1
                    if attempt == max_retry_attempts:
                        print(f"Intento {attempt}: fallo final, lanzando excepción")
                        raise
                    else:
                        wait_time = backoff_factor * (2 ** (attempt - 1))
                        print(
                            f"Intento {attempt}: fallo con {e}, reintentando en {wait_time}s..."
                        )
                        time.sleep(wait_time)

        return wrapper

    return decorator
