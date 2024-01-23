#Loops For/While
nums = [1, 2, 3, 4, 5, 6]
print('-----------------------------------------------------------------')
print('-------------FOR--------------')
for num in nums:
    print(num)
print('-----------------------------------------------------------------')
print('-------------USANDO continue--------------')
for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)

print('-----------------------------------------------------------------')
print('-------------USANDO break--------------')
for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)

print('-----------------------------------------------------------------')
print('-------------USANDO range--------------')

for i in range(10):
    print(i)

print('-----------------------------------------------------------------')
print('-------------lops aninhados--------------')

for num in nums:
    for letter in 'abc':
        print(num, letter)

print('-----------------------------------------------------------------')
print('-------------WHILE--------------')

x = 0

while x < 10:
    print(x)
    x += 1


print('-----------------------------------------------------------------')
print('-------------USANDO break--------------')

y = 0

while y < 10:
    if y == 5:
        print('Metade')
        break
    print(y)
    y += 1

#se fizer um while True sem um break entra em loop infinito