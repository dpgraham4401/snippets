"""Writing an asynchronous socket server using asyncio."""

import socket

# create a socket using IPv4 (AF_INET) and TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# set the SO_REUSEADDR option to reuse the same address, useful if server starts/stops frequently
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address)
server_socket.listen()
# set the socket to non-blocking mode, this is required for the server to actually function with multiple connections
# it allows the server to return buffers to the 2nd client before the connection is closed with the 1st client
server_socket.setblocking(False)

connections = []

try:
    while True:
        try:
            connection, client_address = server_socket.accept()
            connection.setblocking(False) # also need this
            print(f"Connection from {client_address}")
            connections.append(connection)
        except BlockingIOError:
            # See note below on why we need to handle this exception
            pass

        for client in connections:
            try:
                buffer = b''
                while buffer[-2:] != b'\r\n':
                    data = connection.recv(2)
                    if not data:
                        break
                    else:
                        print(f"Received: {data!r}")
                        buffer += data
                print(f"All data received: {buffer!r}")
                client.send(buffer)
            except BlockingIOError:
                # if we put the socket in non-blocking mode, we need to handle this exception
                # essentially, because there is no data to process, the server instantly crashes
                # THIS IS NOT THE REAL WAY TO HANDLE THIS, BUT for example only
                # This is resource intensive and wasteful
                pass
finally:
    server_socket.close()