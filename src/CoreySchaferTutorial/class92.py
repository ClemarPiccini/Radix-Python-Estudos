import itertools

'''
count(start, step): Gera uma sequência infinita de números a partir de start, com um intervalo de step entre eles.

zip_longest(*iterables, fillvalue=None): Combina os elementos de vários iteráveis em tuplas. Se os iteráveis tiverem comprimentos diferentes, o fillvalue é usado para preencher os valores ausentes.

cycle(iterable): Repete os elementos de um iterável indefinidamente.

repeat(obj, times=None): Repete o objeto obj um número de vezes especificado por times.

starmap(function, iterable): Aplica a função function aos elementos do iterável descompactando-os como argumentos.

combinations(iterable, r): Gera todas as combinações possíveis de r elementos do iterável.

permutations(iterable, r=None): Gera todas as permutações possíveis de até r elementos do iterável.

product(*iterables, repeat=1): Calcula o produto cartesiano de vários iteráveis.

chain(*iterables): Combina vários iteráveis em um único iterador.

islice(iterable, stop): Retorna uma fatia do iterável até o índice stop.

compress(data, selectors): Retorna os elementos de data onde o correspondente elemento em selectors for verdadeiro.

filterfalse(predicate, iterable): Retorna os elementos do iterável onde a função predicate retorna falso.

dropwhile(predicate, iterable): Descarta os elementos do iterável enquanto a função predicate retornar verdadeiro e, em seguida, retorna os elementos restantes.

takewhile(predicate, iterable): Retorna os elementos do iterável enquanto a função predicate retornar verdadeiro e, em seguida, para.

accumulate(iterable, func=operator.add): Retorna uma sequência acumulativa dos elementos do iterável, aplicando a função func de acumulação.

groupby(iterable, key=None): Agrupa os elementos do iterável com base no resultado da função key.

tee(iterable, n=2): Produz n iteradores independentes a partir do iterável de entrada.'''

def get_state(person):
    return person['state']


people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]

person_group = itertools.groupby(people, get_state)

copy1, copy2 = itertools.tee(person_group)

for key, group in person_group:
    print(key, len(list(group)))
    # for person in group:
    #     print(person)
    # print()