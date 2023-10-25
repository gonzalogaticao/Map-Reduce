# pip install mrjob
# Cumple con el map-reduce pero:
# (A)- Hasta ahora lee desde un txt.
# (B)- Primero debe leer el numero de la linea a la que corresponde.
# ej: 1 esta es la primera linea
#     2 esta es la segunda linea

from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")


class MRWordFreqCount(MRJob):

    def mapper(self, _, line):
        words = WORD_RE.findall(line)
        for word in words:
            yield (word.lower(), (line, 1))

    def combiner(self, word, line_counts):
        line_count_dict = {}
        for line, count in line_counts:
            if line not in line_count_dict:
                line_count_dict[line] = count
            else:
                line_count_dict[line] += count
        yield (word, list(line_count_dict.items()))

    def reducer(self, word, line_counts_list):
        final_line_count_dict = {}
        for line_counts in line_counts_list:
            for line, count in line_counts:
                if line not in final_line_count_dict:
                    final_line_count_dict[line] = count
                else:
                    final_line_count_dict[line] += count

        output_list = [(self.parse_output(line), count)
                       for line, count in final_line_count_dict.items()]
        yield (word, output_list)

    def parse_output(self, line):
        # Implementa la lógica para extraer el número de línea de la línea original
        # En este caso, se asume que el número de línea está al inicio de la línea.
        parts = line.split(' ', 1)
        if len(parts) == 2 and parts[0].isdigit():
            return int(parts[0])
        else:
            # Manejar la situación en la que no se encuentra un número al inicio de la línea
            return None


if __name__ == '__main__':
    MRWordFreqCount.run()
