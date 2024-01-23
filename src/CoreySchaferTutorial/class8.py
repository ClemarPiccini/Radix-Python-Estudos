#Functions

def hello_func():
    return "isso é uma função."

print(hello_func())

#função com argumentos

def hello_func_arg(greeting, name='You'):
    return '{}, {}'.format(greeting, name)

print(hello_func_arg('Hi', name = 'Junior'))

#funcao um pouco mais complexa

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(*courses, **info)
