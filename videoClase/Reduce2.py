# Al ejecutar: python Mapp.py | python Reduce2.py  
# Imprime en un txt el resultado del map-reduce: palabra{linea,cantidad}
# Tiene problemas con un input sucio, se cae en windows, muestra caracteres extranos en linux.

import sys
from collections import defaultdict

def main():
    indice_invertido = defaultdict(lambda: defaultdict(int))

    for linea in sys.stdin:
        linea = linea.strip()
        if not linea:
            continue

        palabra, numero_linea = linea.split()
        numero_linea = int(numero_linea)

        indice_invertido[palabra][numero_linea] += 1

    with open('Biobio/biobio_reduced.txt', 'w') as f:
        for palabra in sorted(indice_invertido.keys()):
            lineas = indice_invertido[palabra]
            listado = "".join(
                [f"({numero_linea},{conteo})" for numero_linea, conteo in lineas.items()])
            print(f"{palabra}: {listado}", file=f)


if __name__ == "__main__":
    main()
