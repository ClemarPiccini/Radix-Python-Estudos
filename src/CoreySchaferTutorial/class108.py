#Indentação e Espaços - Garanta uma indentação consistente (geralmente 4 espaços) e evite misturar tabs e espaços. Use um editor que suporte a conversão entre tabs e espaços.
# Errado
if True:
#print('Indentação incorreta')

# Correto
    if True:
        print('Indentação correta')

#Conflitos de Nomes - Evite conflitos de nomes usando nomes de variáveis descritivos e evitando palavras-chave reservadas. Use nomes únicos para variáveis, funções e classes.
# Errado
class Class:
    def __init__(self):
        pass

# Correto
class MyClass:
    def __init__(self):
        pass

#Argumentos Padrão Mutáveis - Tenha cuidado com argumentos padrão mutáveis em definições de função. Em vez disso, use objetos imutáveis como None ou especifique o valor padrão dentro do corpo da função.
# Errado
def append_to(element, target=[]):
    target.append(element)
    return target

# Correto
def append_to(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target

#Exaustão de Iteradores - Esteja atento à exaustão de iteradores inadvertidamente, especialmente em loops ou compreensões de lista. Use expressões geradoras ou funções para criar iteradores quando necessário.
# Errado
# iterator = iter(range(3))
# while True:
#     print(next(iterator))

# Correto
iterator = iter(range(3))
try:
    while True:
        print(next(iterator))
except StopIteration:
    pass

#Importando com * (Wildcard) - Evite importar tudo de um módulo usando o * wildcard. Em vez disso, importe funções, classes ou constantes específicas que você precisa usar para manter seu código limpo e legível.
# Errado
#from module import *

# Correto
#from module import function_name