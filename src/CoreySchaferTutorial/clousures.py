#Closures

#Um closure (ou fechamento) em Python é uma função definida dentro de outra função (função externa) e que tem acesso às variáveis locais da função externa, mesmo após a função externa ter retornado. Isso significa que um closure pode "fechar" (capturar) variáveis da função externa e utilizá-las em sua própria lógica.

def outer_function():
    message = 'Hi'

    def inner_function():
        print(message)

    return inner_function()

outer_function()


import logging
logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func


def add(x, y):
    return x+y


def sub(x, y):
    return x-y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3)
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(20, 10)