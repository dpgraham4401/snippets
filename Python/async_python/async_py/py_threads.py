"""Using Threads in Python to handle blocking work.

Even though Python has the GIL, multithreading is a great way to handle IO bound synchronous code,
for example using legacy popular HTTP libraries like requests.
Blocking IO releases the global interpreter lock, enabling the possibility of running IO
concurrently.
"""

from threading import Thread
import socket

import requests


def get_status_code(url: str) -> int:
    response = requests.get(url)
    return response.status_code


if __name__ == "__main__":
    url = "https://www.example.com"
    print(get_status_code(url))
    print(get_status_code(url))
