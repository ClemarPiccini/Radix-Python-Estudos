#Condicionais e bolenaos - If - Else - Elif
'''
== : Verifica se dois valores são iguais.
!= : Verifica se dois valores são diferentes.
> : Verifica se o valor à esquerda é maior que o valor à direita.
< : Verifica se o valor à esquerda é menor que o valor à direita.
>= : Verifica se o valor à esquerda é maior ou igual ao valor à direita.
<= : Verifica se o valor à esquerda é menor ou igual ao valor à direita.
'''

language = input('Qual a linguagem que voce esta aprendendo:').upper()#usei o metodo upper para nao ter erro caso o usuario escreva minusculo ou diferente do esperado
if language == 'PYTHON':
    print('Parabéns acertou!!! Você esta aprendendo {}'.format(language))
elif language == 'JAVA':
    print('Fique longe de {}, ele é perigoso.'.format(language))
else:
    print('Você não esta aprendendo {}.'.format(language))


'''
and( as duas condições devem ser verdadeiras) 
or (apenas uma das condições precisa ser verdadeira)
not (mesma coisa que usar um não é falso)
''' 
user = 'Admin'
logged_in = True

print('UTILIZANDO AND')

if user == 'Admin' and logged_in:
    print('Admin page')
else:
    print('Bad creds')

user = 'Admin'
logged_in = False

print('UTILIZANDO OR')

if user == 'Admin' or logged_in:
    print('Admin page')
else:
    print('Bad creds')

user = 'Admin'
logged_in = True

print('UTILIZANDO NOT')

if not logged_in:
    print('Please Log in')
else:
    print('Welcome Admin')
