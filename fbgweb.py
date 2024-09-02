import os
import sys
import subprocess

# Comprobar si se está usando un entorno virtual
def check_virtual_env():
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        return True
    else:
        return False

# Imprimir si se está usando un entorno virtual o Python global
if check_virtual_env():
    print("[INFO] fbgweb: Ejecutando con un entorno virtual.")
else:
    print("[INFO] fbgweb: Ejecutando con Python global.")

# Imprimir sys.path para depuración
print(sys.path)

# Definir la ruta al archivo fbgweb.py dentro de dependencies
fbgweb_path = os.path.join(os.path.dirname(__file__), 'dependencies', 'fbgweb.py')

def main():
    if len(sys.argv) < 2:
        print("Uso: python fbgweb.py [comando]")
        print("Comandos disponibles: install, reinstall, start, test")
        return

    command = sys.argv[1]

    if os.path.exists(fbgweb_path):
        # Usar sys.executable para asegurar que se use el intérprete correcto
        result = subprocess.run([sys.executable, fbgweb_path, command])
        if result.returncode != 0:
            print(f"Error al ejecutar el comando {command}.")
    else:
        print("El archivo fbgweb.py no se encontró en la carpeta dependencies.")

if __name__ == "__main__":
    main()
