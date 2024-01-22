#strings
my_message = 'Hello World'

big_message = '''Esta é uma mensagem de multiplas linhas,
posso escrever o quanto eu quiser aqui dentro.'''

#len para verificar o comprimento da string
print(len(my_message))

#type para verificar o tipo do valor
print(type(my_message))

#Usamos [] para verificar o que tem no indice.
print(my_message[0])
print(my_message[6:])

#Para pegar um intervalo usamos o indice inicial:indice final
print(big_message[0:4])

#
print(sorted(big_message))

###METODOS

#transformar em minusculo
print(my_message.lower())

#transformar em maiusculo
print(big_message.upper())

#contar quantas vezes o valor aparece na variavel
print(big_message.count('u'))

#procurar onde começa algum valor
print(my_message.find('ld'))

new_message = my_message.replace('World', 'Universe')
print(new_message)

greeting = 'Hello'
name = 'Clemar'

message = f'{greeting}, {name.upper()}. Welcome!'
print(message)

#para verificar os metodos e atributos disponives de um objeto usamos dir.
print(dir(name))

#temos tambem o help, mas esse deve ser usado junto a classe.
print(help(sorted))#aqui podemos passar um metodo junto exemplo o .lowertg