import sys
import os

def check_virtual_env():
    """Verifica si se está usando un entorno virtual."""
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        return True
    else:
        return False

def main():
    if check_virtual_env():
        print("[INFO] Ejecutando con un entorno virtual.")
    else:
        print("[INFO] Ejecutando con Python global.")

    # Imprimir el ejecutable de Python que se está utilizando
    print(f"[INFO] Ejecutable de Python: {sys.executable}")
    
    # Imprimir sys.path para ver qué rutas están incluidas
    print(f"[INFO] sys.path: {sys.path}")

if __name__ == "__main__":
    main()
