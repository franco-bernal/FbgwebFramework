import os
from jinja2 import Environment, FileSystemLoader

def chata():
    # Cargar la plantilla desde la carpeta views
    file_loader = FileSystemLoader('views')
    env = Environment(loader=file_loader)

    # Obtener la plantilla chata.html
    template = env.get_template('chata.html')

    # Obtener la variable SOCKET_INFO desde las variables de entorno
    socket_info = os.getenv('SOCKET_INFO')

    # Datos que queremos pasar a la plantilla
    data = {
        'title': 'FBGWEB',
        'heading': 'FBGWEB Framework',
        'content': 'Este es el contenido de la página de inicio.',
        'socket_info': socket_info  # Pasar la variable SOCKET_INFO a la plantilla
    }

    # Renderizar la plantilla con los datos
    output = template.render(data)

    # Devolver el HTML renderizado
    return output
