#LINK    -     https://www.youtube.com/watch?v=QVdf0LgmICw&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=19


'''
Escopo de Variáveis em Python: O escopo de uma variável em Python se refere à região do código onde a variável é acessível. Isso pode variar dependendo de onde a variável é definida.

Regra LEGB: A regra LEGB é uma convenção que define a ordem de procura de variáveis em Python. Ela significa:

L (Local): Primeiro, o interpretador procura por variáveis no escopo local, ou seja, dentro da função atual.
E (Enclosing): Se a variável não for encontrada no escopo local, o interpretador procura no escopo da função que engloba a função atual.
G (Global): Se a variável ainda não for encontrada, o interpretador procura no escopo global, ou seja, fora de qualquer função.
B (Built-in): Por fim, se a variável não for encontrada nos escopos anteriores, o interpretador procura nas variáveis internas do Python.
Instruções Globais/Não Locais: Em Python, as instruções global e nonlocal são usadas para modificar variáveis fora do escopo local atual.

global: Essa instrução permite que você modifique uma variável global dentro de uma função.
nonlocal: Essa instrução permite que você modifique uma variável em um escopo não local, ou seja, em uma função que envolve a função atual (mas não global).
'''

def funcao_local():
    x = 10 
    print(x)

funcao_local()
print(x)

'''
Escopo Global:
Variáveis definidas fora de qualquer função têm escopo global.
Elas podem ser acessadas de qualquer lugar do código.
'''
y = 20
def funcao_global():
    print(y)

funcao_global()
print(y)


'''
Instrução global:
Permite modificar uma variável global dentro de uma função.
'''
z = 30
def modificar_global():
    global z
    z = 40

print(z)
modificar_global()
print(z)


'''
Instrução nonlocal:
Permite modificar uma variável em um escopo não local (em uma função que engloba a função atual).
'''
def externa():
    x = "escopo externo"
    def interna():
        nonlocal x
        x = "escopo interno"
    interna()
    print(x)

externa()
