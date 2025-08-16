import subprocess

def decodificar():
        base64_texto = input("Introduce el texto en base64: ")  # Leer desde teclado
        resultado = subprocess.run(
            f'echo "{base64_texto}" | base64 -d',
            shell=True,
            capture_output=True,
            text=True
        )
        print("Texto decodificado:", resultado.stdout)

if __name__ == "__main__":
    decodificar()

