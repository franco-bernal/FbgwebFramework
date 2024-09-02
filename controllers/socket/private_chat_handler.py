# controllers/socket/private_chat_handler.py
from classes.socket.websocket_handler import WebSocketHandler


class PrivateChatHandler(WebSocketHandler):
    async def handle(self, id_usuario, data, connection_manager):
        destinatario_id = data.get("destinatario_id")
        mensaje = data.get("mensaje")

        print(f"Mensaje recibido para {destinatario_id}: {mensaje}")
        print(f"Usuarios conectados: {list(connection_manager.active_connections.keys())}")

        if destinatario_id and mensaje:
            await connection_manager.send_message(destinatario_id, mensaje)
        else:
            print(f"Datos incompletos para el mensaje: {data}")

