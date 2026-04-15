import time
from concurrent.futures import ProcessPoolExecutor


def cpu_task(n):
    return sum(i * i for i in range(10_000_000))


def main_pool():
    start = time.time()

    with ProcessPoolExecutor() as executor:
        results = list(executor.map(cpu_task, range(4)))

    print("tiempo de ejecución de cpu con 4 tareas:", time.time() - start)
    return results


def main_pool_less():
    start = time.time()
    for _ in range(4):
        cpu_task(0)
    print(
        "tiempo de ejecución de cpu con 4 tareassin process pool: ", time.time() - start
    )
