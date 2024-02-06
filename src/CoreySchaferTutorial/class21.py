li = [9,1,8,2,7,3,6,4,5]

s_li = sorted(li, reverse = True)

print('Sorted Variable: \t', s_li)

li.sort()

print('Original Variable: \t', li)

tup = (9,1,8,2,7,3,6,4,5)#tuplas sao imutaveis entao copiamos ela para um a lista

s_tup = sorted(tup)

print('Tuple\t', tup)

print('Tuple\t', s_tup)

di = {'name': 'Corey', 'job': 'programming', 'age': None, 'os': 'Mac'}

s_di = sorted (di)


print('Dict\t', s_di)

li = [-6,-5,-4,1,2,3]

s_li = sorted(li, key=abs)#valor absoluto

print (li)

print (s_li)


class Employee():
    def __init__ (self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __repr__ (self):
        return '({},{},${})'.format(self.name, self.age, self.salary)
        
e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1,e2,e3]

def e_sort(emp):
    return emp.name#aqui posso passar outros filtros como salario ou idade no lugar de nome

s_employees = sorted(employees, key=e_sort)

print(s_employees)