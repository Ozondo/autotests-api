import asyncio

import websockets


async def client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = "Привет, Сервер"
        await websocket.send(message)

        for i in range(5):
            response = await websocket.recv()
            print(f"{i+1} {response}")




asyncio.run(client())