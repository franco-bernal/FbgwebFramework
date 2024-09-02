import os
import subprocess
import json
import sys
from datetime import datetime

# Definir la ruta para el archivo de log en la carpeta /logs en la raíz del proyecto
log_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "logs", "dependencies.log")

def log_message(message):
    """Registra un mensaje en el archivo de log y lo muestra en consola."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"[{timestamp}] {message}"
    print(full_message)

    # Asegurarse de que la carpeta /logs existe
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

    with open(log_file_path, "a") as log_file:
        log_file.write(full_message + "\n")

def check_virtual_env():
    """Verifica si se está usando un entorno virtual."""
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        return True
    else:
        return False

def reinstall_requirements():
    """Desinstala y luego reinstala las dependencias listadas en package.json."""
    log_message("Reinstalando dependencias...")

    # Leer el archivo package.json
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "package.json"), "r") as f:
        config = json.load(f)

    dependencies = config.get("dependencies", {})

    # Desinstalar cada dependencia listada en package.json
    for package in dependencies.keys():
        log_message(f"Desinstalando: {package}")
        subprocess.call([sys.executable, "-m", "pip", "uninstall", "-y", package])

    # Reinstalar cada dependencia listada en package.json
    for package, details in dependencies.items():
        version = details.get("version", "")
        log_message(f"Reinstalando: {package}{version}")
        subprocess.call([sys.executable, "-m", "pip", "install", f"{package}{version}"])

def main():
    # Informar si se está usando un entorno virtual o Python global
    if check_virtual_env():
        log_message("[INFO] Ejecutando con un entorno virtual.")
    else:
        log_message("[INFO] Ejecutando con Python global.")

    # Reinstalar las dependencias listadas en package.json
    reinstall_requirements()

if __name__ == "__main__":
    main()
