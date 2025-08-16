import subprocess

def ver_conexiones_establecidas():
    try:
        # Ejecutamos netstat con sudo
        resultado = subprocess.run(
            ["sudo", "netstat", "-tnp"],
            capture_output=True,
            text=True
        )
        
        # Revisamos línea por línea
        print("Conexiones ESTABLISHED:\n")
        for linea in resultado.stdout.splitlines():
            if "ESTABLISHED" in linea:
                print(linea)
    except Exception as e:
        print("Error al ejecutar el comando:", e)

if __name__ == "__main__":
    ver_conexiones_establecidas()

