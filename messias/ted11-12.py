import csv

with open ('filmes.csv', 'r', newline='', encoding='utf-8') as avocado:
    files_read = csv.reader(avocado)
    for line in files_read:
        print(line)