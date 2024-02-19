# Um namedtuple é uma subclasse de tupla com nomes de campo nomeados. Isso significa que, em vez de acessar os elementos por índices numéricos, você pode acessá-los por nomes específicos

from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue'])

color = Color(55,155,255)
white = Color(255,255,255)

print (color.blue)

# list / tuple
color = (55,155,255)

# dictionary
color = {'red': 55, 'green': 155, 'blue': 255}

# namedtuple
Color = namedtuple('Color', ['red', 'green', 'blue'])
color = Color(blue=55,green=155,red=255)


'''
Você deve considerar usar namedtuples em situações em que precisa armazenar dados simples e lembra-se dos campos por nome. Algumas razões para usar namedtuples incluem:

Clareza do código: Em vez de acessar tuplas por índices numéricos, você pode usar nomes de campos que tornam o código mais legível e autoexplicativo.

Imutabilidade: Como as tuplas, namedtuples são imutáveis, o que pode ser útil para garantir que os dados não sejam alterados acidentalmente.

Eficiência: Namedtuples são mais eficientes em termos de uso de memória em comparação com dicionários para armazenar dados simples com um número fixo de campos.
'''