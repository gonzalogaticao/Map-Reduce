#No jala

import json
from mrjob.job import MRJob
import re
import os

WORD_RE = re.compile(r"[\w']+")

class MRWordFreqCount(MRJob):

    def mapper(self, _, line):
        # Obtiene la ruta absoluta del script y construye la ruta del archivo JSON
        script_path = os.path.abspath(__file__)
        json_path = os.path.join(os.path.dirname(script_path), 'noticias.json')

        # Carga el contenido de la noticia desde el archivo JSON
        with open(json_path, 'r') as archivo:
            datos = json.load(archivo)
            
        for noticia in datos['noticias']:
            contenido = noticia['contenido']
            words = WORD_RE.findall(contenido)
            for word in words:
                yield (word.lower(), 1)

    def combiner(self, word, counts):
        yield (word, sum(counts))

    def reducer(self, word, counts):
        yield (word, sum(counts))

if __name__ == '__main__':
    MRWordFreqCount.run()
