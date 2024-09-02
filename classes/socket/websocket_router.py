# classes/socket/websocket_router.py
import json

class WebSocketRouter:
    def __init__(self):
        self.routes = {}

    def add_route(self, message_type, handler, **kwargs):
        self.routes[message_type] = (handler, kwargs)

    async def route_message(self, id_usuario, message, connection_manager):
        try:
            data = json.loads(message)
            message_type = data.get("tipo")
            handler_entry = self.routes.get(message_type)
            if handler_entry:
                handler, handler_params = handler_entry
                print(f"Enrutando mensaje de tipo {message_type} al manejador.")
                await handler.handle(id_usuario, data, connection_manager, **handler_params)
            else:
                print(f"No se encontró un manejador para el tipo de mensaje: {message_type}")
        except json.JSONDecodeError:
            print("Error al decodificar el mensaje JSON.")
