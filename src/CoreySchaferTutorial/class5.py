#Dicionarios

student = {'name': 'John', 'age': '24', 'courses': ['math', 'hystori']}

for key, value in student.items():
    print(key, value)

# Acessando valores no dicionário
print(student['name'])
print(student['age'])
print(student['courses'])

# Adicionando um novo par chave-valor ao dicionário
student['nota'] = '8'
print(student)

# Modificando um valor no dicionário
student['age'] = 21
print(student)

# Removendo um par chave-valor do dicionário
del student['nota']
print(student)