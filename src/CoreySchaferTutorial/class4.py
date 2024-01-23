# Listas
courses = ['matematica', 'historia', 'geografia', 'artes']
print(courses)
print(len(courses))  # Imprime o comprimento da lista (número de elementos)
print(courses[0])  # Imprime o primeiro elemento da lista (índice 0)

courses.append('fisica') 
courses.reverse()  # Inverte a ordem dos elementos na lista
print(courses)

# Métodos adicionais de lista:
# .sort() ordena os elementos em ordem alfabética
# .pop() remove e retorna o último elemento da lista

# Tuplas
number = ('historia', 'matematica', 'artes', 'fisica')

# Tuplas são semelhantes às listas, mas são imutáveis, ou seja, não podem ser modificadas após a criação.

# Sets
sets = {'historia', 'matematica', 'artes', 'fisica'}
# Os conjuntos (sets) em Python são coleções desordenadas de elementos únicos. Eles não permitem elementos duplicados e não possuem ordem definida.
# Os conjuntos têm operações úteis, como união, interseção e diferença, que podem ser úteis para operações de conjunto.
