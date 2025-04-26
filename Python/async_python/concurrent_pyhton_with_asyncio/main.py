"""Writing an echo socket server using asyncio."""

import asyncio
from asyncio import AbstractEventLoop

import socket


async def echo(connection: socket, loop: AbstractEventLoop) -> None:
    """Echo messages from a client."""
    while data := await loop.sock_recv(connection, 1024):
        print(f"Received {data!r}")
        await loop.sock_sendall(connection, data)


async def listen_for_connection(server_socket: socket, loop: AbstractEventLoop):
    """Listen for incoming connections.

    This function has the same role as our while loop in the previous version.
    """
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f"Got a connection from {address}")
        asyncio.create_task(echo(connection, loop))


async def main():
    """Set up the server and listen for incoming connections."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ("127.0.0.1", 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()
    await listen_for_connection(server_socket, asyncio.get_event_loop())


if __name__ == "__main__":
    asyncio.run(main())
