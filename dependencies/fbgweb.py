import sys
import os
import subprocess
from datetime import datetime

# Definir la ruta para el archivo de log en la carpeta /logs en la raíz del proyecto
log_file_path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'dependencies.log')

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

def run_command(command):
    """Ejecuta el comando especificado."""
    command_path = os.path.join(os.path.dirname(__file__), 'commands', f'{command}.py')
    if os.path.exists(command_path):
        log_message(f"Ejecutando comando: {command}")
        # Usar subprocess.run con sys.executable para asegurar que se use el intérprete correcto
        result = subprocess.run([sys.executable, command_path])
        if result.returncode != 0:
            log_message(f"Hubo un error al ejecutar el comando: {command}")
    else:
        log_message(f"Comando '{command}' no encontrado.")
        print(f"Comando '{command}' no encontrado.")

def main():
    if check_virtual_env():
        log_message("[INFO] fbgweb dep: Ejecutando con un entorno virtual.")
    else:
        log_message("[INFO] fbgweb dep: Ejecutando con Python global.")

    if len(sys.argv) < 2:
        log_message("Uso: python fbgweb.py [comando]")
        log_message("Comandos disponibles: install, reinstall, start, test")
        print("Uso: python fbgweb.py [comando]")
        print("Comandos disponibles: install, reinstall, start, test")
        return

    command = sys.argv[1]

    if command in ["install", "reinstall", "start", "test"]:
        run_command(command)
    else:
        log_message(f"Comando desconocido: {command}")
        log_message("Comandos disponibles: install, reinstall, start, test")
        print(f"Comando desconocido: {command}")
        print("Comandos disponibles: install, reinstall, start, test")

if __name__ == "__main__":
    main()
