try:
    with open("../Biobio/biobio_pages.txt", "r", encoding="utf-8") as archivo, \
         open("../Biobio/Mapped-Biobio.txt", "a", encoding="utf-8") as f:
        for num_linea, linea in enumerate(archivo, start=1):
            palabras = linea.lower().split()
            for palabra in palabras:
                f.write(f"{palabra} {num_linea}\n")
except FileNotFoundError:
    print("Error: Could not find the specified file.")
except PermissionError:
    print("Error: You do not have permission to access the specified file.")

