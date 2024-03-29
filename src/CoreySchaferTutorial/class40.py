#Classes and Instances

class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

emp_1 = Employee('Junior', 'Piccini', 50000)
emp_2 = Employee('Teste', 'User', 60000)

print(emp_1.email)
print(emp_1.fullname())