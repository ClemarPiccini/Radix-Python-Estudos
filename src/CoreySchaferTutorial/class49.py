with open('arquivo.txt', 'r') as f:
    conteudo = f.read()
    # faça algo com o conteúdo do arquivo

# Neste ponto, o arquivo já foi fechado automaticamente, 
# independentemente do que aconteceu no bloco `with`.

class MeuContexto:
    def __enter__(self):
        # Faça algo ao entrar no contexto
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Faça algo ao sair do contexto
        pass

# Uso do contexto personalizado
with MeuContexto() as contexto:
    # Faça algo dentro do contexto
    pass