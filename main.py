import asyncio
import websockets

async def hello(websocket):
    while True:
        try:
            structure_description = await websocket.recv()
        except websockets.ConnectionClosed:
            print(f"Terminated")
            break

        print(f"< {structure_description}")
        structure_nodes = f"{structure_description}$"

        await websocket.send(structure_nodes)
        print(f"> {structure_nodes}")

start_server = websockets.serve(hello, "localhost", 3001)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()