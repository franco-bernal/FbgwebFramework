
# FbgwebFramework

**FbgwebFramework** es un framework ligero y modular diseñado para facilitar el desarrollo de aplicaciones web utilizando Python. Este framework está pensado para ser simple, flexible y fácil de extender, permitiendo a los desarrolladores centrarse en la lógica de su aplicación sin perder tiempo en configuraciones complejas.

## Características

- **Rutas Dinámicas**: Define rutas HTTP de manera sencilla.
- **Soporte para WebSockets**: Integración nativa con WebSockets para aplicaciones en tiempo real.
- **Motor de Plantillas Jinja2**: Renderiza plantillas HTML utilizando el potente motor Jinja2.
- **Fácil Configuración**: Configuración centralizada mediante un archivo `.env`.
- **Soporte para Servidores HTTP y WebSocket**: Ejecuta tanto servidores HTTP como WebSocket de manera integrada.

## Requisitos

- Python 3.8 o superior
- Entorno virtual (recomendado)

## Instalación

1. Clona este repositorio en tu máquina local:

    ```bash
    git clone https://github.com/tu-usuario/FbgwebFramework.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd FbgwebFramework
    ```

3. (Opcional) Crea y activa un entorno virtual:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # En Windows: .venv\Scriptsctivate
    ```

4. Instala las dependencias utilizando el comando del framework:

    ```bash
    python fbgweb.py install
    ```

## Uso

1. Configura las variables de entorno en el archivo `.env` ubicado en la raíz del proyecto.

2. Ejecuta el servidor:

    ```bash
    python fbgweb.py start
    ```

3. Accede a la aplicación desde tu navegador en `http://localhost:[PUERTO]`.

## Reinstalación de Dependencias

Si necesitas reinstalar todas las dependencias, puedes utilizar el siguiente comando:

```bash
python fbgweb.py reinstall
```

## Estructura del Proyecto

```
FbgwebFramework/
│
├── app/                 # Código principal de la aplicación
├── classes/             # Clases base y utilidades
├── views/               # Plantillas HTML
├── routes/              # Definición de rutas
├── socket/              # Configuración de WebSockets
├── fbgweb.py            # Script principal del framework
├── README.md            # Este archivo
└── requirements.txt     # Dependencias del proyecto
```

## Contribuir

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una rama nueva (`git checkout -b feature-nueva-funcionalidad`).
3. Realiza los cambios necesarios y haz un commit (`git commit -m 'Añadir nueva funcionalidad'`).
4. Envía tus cambios a tu repositorio (`git push origin feature-nueva-funcionalidad`).
5. Abre una Pull Request.

## Licencia

Este proyecto está licenciado bajo la [MIT License](https://opensource.org/licenses/MIT) - mira el archivo `LICENSE` para más detalles.

## Contacto

Si tienes preguntas o sugerencias, no dudes en contactarme a través de [franco.bernalgutierrez@gmail.com](mailto:franco.bernalgutierrez@gmail.com).
