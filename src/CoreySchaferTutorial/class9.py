#Import Modules and Exploring The Standard Library
#importando a funcao find_index e a variavel test
from my_module_class9 import find_index, test

courses = ['Hystory', 'Math', 'Art', 'CompSci']
#utilizando a funcao criada em outro arquivo
index = find_index(courses, 'Math')
print(index)

#utilizando a variavel criada em outro arquivo
print(test)

#até aqui as aulas estao em sequencia, após isso podemos decidir qual conteudo ver e seguir de forma não sequencial.
