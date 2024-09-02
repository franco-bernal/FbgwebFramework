# classes/socket/websocket_handler.py
from abc import ABC, abstractmethod

class WebSocketHandler(ABC):
    @abstractmethod
    async def handle(self, id_usuario, data, connection_manager):
        pass
