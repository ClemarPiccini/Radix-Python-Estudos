def add_employee(emp, emp_list=[]):
    emp_list.append(emp)
    print(emp_list)

def add_employee_fixed(emp, emp_list=None):
    if emp_list is None:
        emp_list = []
    emp_list.append(emp)
    print(emp_list)


emps = ['Jhon', 'Jane']

#add_employee('Junior', emps)

add_employee('Junior')
add_employee('Jack')

add_employee_fixed('Taylor')
add_employee_fixed('Robin')


import time
from datetime import datetime
def display_time(time_to_print=datetime.now()):
    print(time_to_print.strftime('%B %d, %Y %H:%M:%S'))


display_time()
time.sleep (1)
display_time()
time.sleep(1)
display_time()