# Funcional.
# Enlista las palabras en 'contenido' según su 'numero' correspondiente.

import json

try:
    with open("Biobio/biobio.json", "r", encoding="utf-8") as archivo_json, \
            open("Biobio/mapped-Biobio.txt", "a", encoding="utf-8") as f:
        datos = json.load(archivo_json)

        for noticia in datos.get("noticias", []):
            num_linea = noticia.get("numero", 0)
            contenido_palabras = noticia.get("contenido", "").lower().split()

            for palabra in contenido_palabras:
                f.write(f"{palabra} {num_linea}\n")

except FileNotFoundError:
    print("Error: No se pudo encontrar el archivo JSON especificado.")
except PermissionError:
    print("Error: No tienes permiso para acceder al archivo JSON especificado.")
except json.JSONDecodeError:
    print("Error: El archivo JSON no tiene un formato válido.")

