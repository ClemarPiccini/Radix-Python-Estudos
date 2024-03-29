# Analisando nomes de um CSV para uma lista HTML

import csv

html_output = ''
names = []

with open('src\CoreySchaferTutorial\patrons.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)

    next(csv_data)

    for line in csv_data:
        if line['FirstName'] == 'No Reward':
            break
        names.append(f"{line['FirstName']} {line['LastName']}")

html_output += f'<p>There are currently {len(names)} public contributors. Thank You!</p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

print(html_output)