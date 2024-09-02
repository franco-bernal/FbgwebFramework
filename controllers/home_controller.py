from jinja2 import Environment, FileSystemLoader

def home():
    # Cargar la plantilla desde la carpeta views
    file_loader = FileSystemLoader('views')
    env = Environment(loader=file_loader)

    # Obtener la plantilla home.html
    template = env.get_template('home.html')

    # Datos que queremos pasar a la plantilla
    data = {
        'title': 'FBGWEB',
        'heading': 'FBGWEB Framework',
        'content': 'Este es el contenido de la página de inicio.',
    }

    # Renderizar la plantilla con los datos
    output = template.render(data)

    # Devolver el HTML renderizado
    return output
