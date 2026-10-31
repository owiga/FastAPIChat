from fastapi import WebSocket

from models.db import (
  database,
)

class ConnectionManager:

  def __init__(self):
    self.active_connections: list[WebSocket] = []

  async def connect(self, websocket: WebSocket):
    await websocket.accept()
    self.active_connections.append(websocket)
    rows = database.get_history()
    for row in reversed(rows):
      await websocket.send_text(row[0])

  def disconnect(self, websocket: WebSocket):
    self.active_connections.remove(websocket)

  async def get_online(self):
    return len(self.active_connections)

  async def broadcast(self, message: str):
    # Рассылаем текст абсолютно всем активным сокетам
    for connection in self.active_connections:
      try:
        await connection.send_text(message)
      except Exception:
        pass