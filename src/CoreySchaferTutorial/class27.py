import random

value = random.uniform(1 ,10)
print(value)

value = random.random()
print(value)

value = random.randint(1, 6)
print(value)


list =[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
value = random.choice(list)
print(value)

color = ['red', 'green', 'black']
value= random.choices(color, weights=[18, 18, 2], k=10) #weights sao as probabilidades de cada numero ser escolhido
print(value)

deck = list(range(1, 53))
random.shuffle(deck)
hand = random.sample(deck, k=5)
print(hand)