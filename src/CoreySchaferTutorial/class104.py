#Condicional Ternária: Uma maneira concisa de escrever uma expressão condicional em uma linha. Por exemplo, resultado = "par" if x % 2 == 0 else "ímpar".
 
x = 10
resultado = "par" if x % 2 == 0 else "ímpar"
print(resultado)

# Espaços Substituídos por Underlines: Uma técnica para tornar números mais legíveis ao substituir os espaços por underlines. Por exemplo, 1_000_000 é mais legível do que 1000000.

numero_grande = 1_000_000
print(numero_grande)

# Gerenciadores de Contexto: Uma forma de garantir a execução de determinado código antes e depois de uma operação, como abrir e fechar um arquivo. Por exemplo, with open('arquivo.txt', 'r') as arquivo: conteudo = arquivo.read().

with open('arquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()

# Enumerar: Uma função útil para obter tanto o índice quanto o valor de uma lista. Por exemplo, for indice, valor in enumerate(lista): print(f"O índice {indice} contém o valor {valor}").

lista = ['a', 'b', 'c']
for indice, valor in enumerate(lista):
    print(f"O índice {indice} contém o valor {valor}")

# Zip: Uma função para combinar duas ou mais listas em pares de elementos correspondentes. Por exemplo, list(zip([1, 2, 3], ['a', 'b', 'c'])) retorna [(1, 'a'), (2, 'b'), (3, 'c')].

lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
for item1, item2 in zip(lista1, lista2):
    print(item1, item2)

# Desempacotamento: Uma técnica para atribuir os elementos de uma lista ou tupla a variáveis individuais. Por exemplo, a, b = [1, 2].

a, b = [1, 2]
print(a, b)

# Setattr/Getattr: Funções para definir e obter atributos de objetos dinamicamente. Por exemplo, setattr(objeto, 'atributo', valor) e getattr(objeto, 'atributo').

class Objeto:
    pass

obj = Objeto()
setattr(obj, 'atributo', 'valor')
print(getattr(obj, 'atributo'))

# GetPass: Uma função para ocultar a entrada de senha do usuário. Por exemplo, senha = getpass.getpass("Digite sua senha:").

import getpass
senha = getpass.getpass("Digite sua senha:")
print(senha)

# Python Dash M: Uma opção de linha de comando para executar scripts Python como módulos. Por exemplo, python -m meu_script.

'''
Executando um script Python como módulo
python -m meu_script
'''
# Help/Dir: Funções úteis para obter informações sobre objetos em Python. Por exemplo, help(objeto) fornece ajuda sobre o objeto e dir(objeto) lista seus atributos e métodos.

lista = [1, 2, 3]
print(help(lista))
print(dir(lista))
