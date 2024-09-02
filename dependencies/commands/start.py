import os
import subprocess
import sys
import signal

# Funciones para agregar colores a la salida
def print_info(message):
    print(f"\033[94m[INFO]\033[0m {message}")

def print_success(message):
    print(f"\033[92m[SUCCESS]\033[0m {message}")

def print_warning(message):
    print(f"\033[93m[WARNING]\033[0m {message}")

def print_error(message):
    print(f"\033[91m[ERROR]\033[0m {message}")

# Verificar si se está usando un entorno virtual
def check_virtual_env():
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        return True
    else:
        return False

# Manejar la señal de interrupción Ctrl+C
def signal_handler(sig, frame):
    print_warning("\n[WARNING] Ejecución interrumpida por el usuario (Ctrl+C).")
    sys.exit(0)

# Asociar la señal SIGINT con el manejador
signal.signal(signal.SIGINT, signal_handler)

def main():
    # Verificar si se está usando un entorno virtual
    if check_virtual_env():
        print_info("[INFO] start.py: Ejecutando con un entorno virtual.")
    else:
        print_info("[INFO] start.py: Ejecutando con Python global.")

    # Obtener la ruta al archivo main.py en la raíz del proyecto
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    main_path = os.path.join(project_root, 'main.py')

    # Mostrar la ruta para depuración
    print_info(f"Iniciando proyecto. Obteniendo enlace... {main_path}")

    # Agregar manualmente el site-packages del entorno virtual al sys.path
    venv_path = os.path.join(project_root, '.venv', 'Lib', 'site-packages')
    if venv_path not in sys.path:
        sys.path.append(venv_path)
    print_info(f"sys.path en start.py: {sys.path}")

    # Ejecutar main.py si existe
    if os.path.exists(main_path):
        # Asegurarse de que se use el entorno virtual correcto
        env = os.environ.copy()
        env['PYTHONPATH'] = venv_path + os.pathsep + env.get('PYTHONPATH', '')
        result = subprocess.run([sys.executable, main_path], cwd=project_root, env=env)
        if result.returncode == 0:
            print_success("main.py se ejecutó correctamente.")
        else:
            print_error("Hubo un error al ejecutar main.py.")
    else:
        print_error("El archivo main.py no se encontró en la raíz del proyecto.")

if __name__ == "__main__":
    main()
