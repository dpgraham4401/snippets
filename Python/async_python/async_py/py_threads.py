"""Using Threads in Python to handle blocking work.

Even though Python has the GIL, multithreading is a great way to handle IO bound synchronous code, 
for example using legacy popular HTTP libraries like requests.
Blocking IO releases the global interpreter lock, enabling the possibility of running IO 
concurrently.
"""

from threading import Thread
import socket

def echo(client: socket.socket):
    while True:
        data = client.recv(2048)
        print(f"received {data!r}, sending!")
        client.sendall(data)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('127.0.0.1', 8000))
    server.listen()
    while True:
        connection, _ = server.accept()
        thread = Thread(target=echo, args=(connection,))
        thread.start()