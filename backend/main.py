from fastapi import FastAPI, WebSocket

app = FastAPI()

clients = []

@app.websocket("/ws")
async def test(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            for client in clients:
                await client.send_text(data)
                
    except WebSocketDisconnect:
        clients.remove(websocket)
        