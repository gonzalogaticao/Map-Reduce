with open(f"Biobio/biobio_pages.txt", "r", encoding="utf-8") as archivo:
    for num_linea, linea in enumerate(archivo, start=1):
        palabras = linea.lower().split()
        for palabra in palabras:
            print(f"{palabra} {num_linea}")
