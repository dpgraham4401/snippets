"""Writing an asynchronous socket server using asyncio."""

import socket

# create a socket using IPv4 (AF_INET) and TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# set the SO_REUSEADDR option to reuse the same address, useful if server starts/stops frequently
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address)
server_socket.listen()

try:
    connection, client_address = server_socket.accept()
    print(f"Connection from {client_address}")
    buffer = b''
    while buffer[-2:] != b'\r\n':
        data = connection.recv(2)
        if not data:
            break
        else:
            print(f"Received: {data}")
            buffer += data
    print(f"All data received: {buffer}")
finally:
    server_socket.close()