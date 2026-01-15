import asyncio


import websockets
from websockets import ServerConnection


async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Received: {message}")
        response = f"Server response: {message}"

        for _ in range(10):
            await websocket.send(response)


async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("Websocket server started on port 8765")

    await server.wait_closed()


asyncio.run(main())