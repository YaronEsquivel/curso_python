import time

import requests


def fetch_sync():
    urls = ["https://jsonplaceholder.typicode.com/users"] * 10

    start = time.time()

    for url in urls:
        fetch(url)

    print("tiempo sincrono de 10 peticiones:", time.time() - start)


def fetch(url):
    return requests.get(url).status_code
