#Decorators

def decorador(func):
    def wrapper():
        print("Antes de chamar a função")
        func()
        print("Depois de chamar a função")
    return wrapper

@decorador
def funcao_decorada():
    print("Função decorada!")

funcao_decorada()


def decorador_com_argumento(argumento):
    def decorador(func):
        def wrapper(*args, **kwargs):
            print(f"Decorando com argumento {argumento}")
            func(*args, **kwargs)
        return wrapper
    return decorador

@decorador_com_argumento("hello")
def funcao_decorada_com_argumento(nome):
    print(f"Olá, {nome}!")

funcao_decorada_com_argumento("João")
