import re

patron = re.compile(r'^J\w+\s+Neu', re.IGNORECASE)

with open('Agenda_Simpsons.txt', 'r') as archivo:
    for linea in archivo:
        if patron.search(linea):
            print(linea.strip())