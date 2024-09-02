# routes/socket.py
from classes.socket.websocket_router import WebSocketRouter
from controllers.socket.private_chat_handler import PrivateChatHandler

# from controllers.socket.group_chat_handler import GroupChatHandler

# Crear una instancia del router
router = WebSocketRouter()

# Registrar las rutas con parámetros
router.add_route('chat_privado', PrivateChatHandler())
# router.add_route('chat_grupal', GroupChatHandler())
