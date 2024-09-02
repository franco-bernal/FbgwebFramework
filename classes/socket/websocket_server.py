import asyncio
import websockets
from classes.socket.websocket_router import WebSocketRouter
from classes.socket.connection_manager import ConnectionManager

class WebSocketServer:
    def __init__(self, host='localhost', port=None):
        self.host = host
        self.port = port if port is not None else 12345
        self.router = WebSocketRouter()
        self.connection_manager = ConnectionManager()
        self.server = None
        self.loop = asyncio.get_event_loop()
        self.active = False

    async def handle_client(self, websocket, path):
        id_usuario = path.strip("/")
        print(f"Registrando usuario con ID: {id_usuario}")  # Agregado para depuración
        await self.connection_manager.register(id_usuario, websocket)
        try:
            async for message in websocket:
                print(f"Mensaje recibido de {id_usuario}: {message}")
                await self.router.route_message(id_usuario, message, self.connection_manager)
        finally:
            await self.connection_manager.unregister(id_usuario)

    def run(self):
        self.server = websockets.serve(self.handle_client, self.host, self.port)
        server_instance = self.loop.run_until_complete(self.server)
        actual_port = server_instance.sockets[0].getsockname()[1]
        print(f"WebSocket server está utilizando el puerto {actual_port} en {self.host}")
        self.active = True
        self.loop.run_forever()

    def stop(self):
        if self.active and self.server:
            self.server.ws_server.close()
            self.active = False
            print("WebSocket server detenido")

    def status(self):
        return "active" if self.active else "inactive"
