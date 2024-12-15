"""Writing an asynchronous socket server using asyncio."""

import socket
# The selectors module "provides high-level and efficient I/O multiplexing"
# simply put, it allows us to wait for events (readable, writable, etc.) on multiple file-like objects (sockets, files, etc.)
# without blocking
import selectors
from selectors import SelectorKey

# Instead of constantly looping and checking for connections from clients, we can use the selectors module
selector = selectors.DefaultSelector()

# create a socket using IPv4 (AF_INET) and TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# set the SO_REUSEADDR option to reuse the same address, useful if server starts/stops frequently
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8000)
server_socket.setblocking(False)
server_socket.bind(server_address)
server_socket.listen()

# Here, we register the socket (remember, everything is a file in Unix) with the selector
# with the event we want to wait for (in this case, read events)
selector.register(server_socket, selectors.EVENT_READ)

while True:
    # infinite loop, and check for an event every second
    events: list[tuple[SelectorKey, int]] = selector.select(timeout=1)
    if len(events) == 0:
        print("Waiting for events...")
    for event, _ in events:
        # get the event's file object
        event_socket = event.fileobj

        # if the event is the server socket, we accept the connection
        if event_socket == server_socket:
            connection, client_address = server_socket.accept()
            connection.setblocking(False)
            print(f"Connection from {client_address}")
            selector.register(connection, selectors.EVENT_READ)
        # otherwise, receive data from the client and send it back
        else:
            data = event_socket.recv(1024)
            print(f"Received: {data!r}")
            event_socket.send(data)
