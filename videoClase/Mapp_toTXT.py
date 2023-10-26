# Funcional.
# Enlista las palabras según su linea correspondiente.

try:
    with open("Biobio/biobio_pages.txt", "r", encoding="utf-8") as archivo, \
         open("Biobio/mapped-Biobio.txt", "a", encoding="utf-8") as f:
        for num_linea, linea in enumerate(archivo, start=1):
            palabras = linea.lower().split()
            for palabra in palabras:
                f.write(f"{palabra} {num_linea}\n")
except FileNotFoundError:
    print("Error: No se pudo encontrar el archivo especificado.")
except PermissionError:
    print("Error: No tienes permiso para acceder al archivo especificado.")

