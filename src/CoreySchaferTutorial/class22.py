# ###STRINGS###

person = {'name': 'Junior', 'age': 23}

sentece = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
print(sentece)

sentence = 'My name is {} and I am {} years old. '.format(person['name'], person['age']) 
print(sentence)

sentence =  'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
print(sentence)

tag = 'hi'
text = 'This is a headline'

sentence = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence)

l = ['Jenn', 23]

sentence = 'My name is {0[0]} and I am {0[1]} years old.'.format(l) 
print(sentence)

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age


pl = Person('Jack', '33')

sentence =  'My name is {0.name} and I an {0.age} years old.'.format(pl) 
print(sentence)

sentence =  'My name is {name} and I an {age} years old.'.format(name='John', age='30') 
print(sentence)

sentence =  'My name is {name} and I an {age} years old.'.format(**person) 
print(sentence)


###NUMBERS###

for i in range(1, 11):
    sentence = 'The value is {:03}'.format(i)
    print(sentence)

pi = 3.14159265

sentence = 'Pi is equal to {:.2f}'.format(pi)
print(sentence)

sentence = '1 MB is equal to {:,} bytes'.format(1000**2)
print(sentence)


###DATETIME###

import datetime 
my_date = datetime.datetime.now() #.now pega os valores da maquina local
print(my_date)

#March 61, 2016

sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)

#March 01, 2016 fell on a Tuesday and was the 061 day of the year.

sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date) 
print(sentence)