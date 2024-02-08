#CSV
import csv

csv_file_path = r'C:\Users\Junior\Downloads\names.csv'

with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Exemplo: Acessar valores específicos
    for line in csv_reader:
        print(f"First Name: {line[0]}, Last Name: {line[1]}")

    # Exemplo: Filtrar linhas com base em condições
    for line in csv_reader:
        if line[2] == 'Male':
            print(f"Male: {line}")

    # Exemplo: Escrita em arquivo CSV
    with open('output.csv', 'w', newline='') as output_file:
        csv_writer = csv.writer(output_file)
        csv_writer.writerow(['First Name', 'Last Name'])
        for line in csv_reader:
            csv_writer.writerow([line[0], line[1]])
