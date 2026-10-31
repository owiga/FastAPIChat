import psutil
import asyncio

from fastapi import WebSocket, WebSocketDisconnect, APIRouter

from models import connection
from models.db import (
    database,
)


router = APIRouter(prefix="")
connectin_manager = connection.ConnectionManager()

@router.websocket("/systemws")
async def index(websocket: WebSocket):
    await websocket.accept()

    while True:
        try:
            p = psutil.cpu_percent(interval=None)
            m = psutil.virtual_memory().percent
            online = await connectin_manager.get_online()

            data = {"cpu": p, "ram": m, "online": online}

            await websocket.send_json(data)
            await asyncio.sleep(0.7)

        except WebSocketDisconnect:
            print("Disconnected SYSTEMWS")
            break

@router.websocket("/chatws")
async def chat_endpoint(websocket: WebSocket):
  await connectin_manager.connect(websocket)
  try:
    while True:
      text = await websocket.receive_text()
      database.add_message(text)
      await connectin_manager.broadcast(text)
  except WebSocketDisconnect:
    connectin_manager.disconnect(websocket)