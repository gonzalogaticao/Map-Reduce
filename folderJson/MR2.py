from mrjob.job import MRJob
import re
import json

WORD_RE = re.compile(r"[\w']+")


class MRWordFreqCount(MRJob):

    def mapper(self, _, line):
        # Parsea la línea como JSON
        data = json.loads(line)
        for obj in data:
            # Extrae el campo "contenido"
            contenido = obj.get('contenido')
            if contenido:
                words = WORD_RE.findall(contenido)
                for word in words:
                    yield (word.lower(), (contenido, 1))

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
        parts = line.split(" ", 1)
        if len(parts) == 2 and parts[0].isdigit():
            return int(parts[0])
        else:
            return None


if __name__ == '__main__':
    MRWordFreqCount.run()