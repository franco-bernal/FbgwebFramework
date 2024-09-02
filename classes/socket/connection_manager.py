# classes/socket/connection_manager.py
class ConnectionManager:
    def __init__(self):
        self.active_connections = {}  # Diccionario para almacenar conexiones activas

    async def register(self, id_usuario, websocket):
        self.active_connections[id_usuario] = websocket
        print(f"Usuario {id_usuario} registrado con WebSocket {websocket}")

    async def unregister(self, id_usuario):
        if id_usuario in self.active_connections:
            del self.active_connections[id_usuario]
            print(f"Usuario {id_usuario} desregistrado.")

    async def send_message(self, id_usuario, message):
        websocket = self.active_connections.get(id_usuario)
        if websocket:
            await websocket.send(message)
            print(f"Mensaje enviado a {id_usuario}: {message}")
        else:
            print(f"No se encontró el websocket para {id_usuario}.")


    async def broadcast(self, message):
        for websocket in self.active_connections.values():
            await websocket.send(message)
