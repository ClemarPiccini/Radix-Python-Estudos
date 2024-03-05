#Python Quick Tip: The Difference Between "==" and "is" (Equality vs Identity)

'=='#verifica se os objetos sao iguais

'is' #verifica se o objeto é o messmo


a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True, porque os valores de a e b são iguais
print(a is b)  # False, porque a e b são objetos diferentes na memória

print(a == c)  # True, porque os valores de a e c são iguais
print(a is c)  # True, porque a e c são o mesmo objeto na memória
