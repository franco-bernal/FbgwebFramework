import sys
import os
import socket
from http.server import HTTPServer
from fbgrouter.classes.request_handler import RequestHandler
from fbgrouter.classes.router import Router

# Mostrar la ubicación del módulo fbgrouter
print(f"fbgrouter se está importando desde: {Router.__module__}")
print(f"Ubicación del archivo: {sys.modules[Router.__module__].__file__}")

from dotenv import load_dotenv
from classes.socket.websocket_server import WebSocketServer

import routes.socket as socket_routes  # Importar las rutas de WebSocket
import threading

# Cargar las variables desde el archivo .env
load_dotenv()

# Obtener las variables del archivo .env
host = os.getenv('HOST')
port = int(os.getenv('PORT', 0))
ws_port = int(os.getenv('WS_PORT', 0))  # Puerto para el servidor WebSocket (0 para automático)

# Determinar la dirección del servidor HTTP
if host.lower() == 'localhost':
    server_address = ('localhost', port)
elif host:  # Si se proporciona una IP en HOST, úsala
    server_address = (host, port)
else:  # Si HOST está vacío, detectar la IP automáticamente
    detected_ip = socket.gethostbyname(socket.gethostname())
    server_address = (detected_ip, port)

def obtener_puerto_disponible():
    """Función para obtener un puerto disponible automáticamente."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        puerto_disponible = s.getsockname()[1]
    return puerto_disponible

def run_http_server(server_class=HTTPServer, handler_class=RequestHandler):
    httpd = server_class(server_address, handler_class)

    # Obtener el puerto asignado (en caso de que se haya asignado dinámicamente)
    assigned_port = httpd.server_address[1]

    print(f'HTTP Server running on http://{server_address[0]}:{assigned_port}...')
    httpd.serve_forever()

def run_websocket_server():
    global ws_port

    # Si ws_port es 0, obtener un puerto disponible automáticamente
    if ws_port == 0:
        ws_port = obtener_puerto_disponible()

    ws_server = WebSocketServer(host=server_address[0], port=ws_port)
    ws_server.router = socket_routes.router

    # Verificar el estado antes de iniciar
    if ws_server.status() == "inactive":
        print(f'WebSocket Server running on ws://{server_address[0]}:{ws_port}...')
        
        # Guardar el número de puerto en una variable de entorno
        os.environ['SOCKET_INFO'] = f"{ws_port}"
        
        # Mostrar la información guardada
        print(f'SOCKET_INFO variable de entorno establecida en: {os.environ["SOCKET_INFO"]}')
        
        ws_server.run()
    else:
        print("WebSocket Server ya está activo.")

if __name__ == "__main__":
    # Iniciar el servidor HTTP en un hilo separado
    http_thread = threading.Thread(target=run_http_server)
    http_thread.start()

    # Iniciar el servidor WebSocket
    run_websocket_server()
