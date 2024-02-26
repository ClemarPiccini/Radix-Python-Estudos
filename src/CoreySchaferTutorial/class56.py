#essa estrutura permite que você defina um ponto de entrada claro para o seu código quando ele é executado diretamente, enquanto ainda permite que ele seja importado como um módulo em outros arquivos sem executar o código de inicialização automaticamente.

def main():
    print('main')
    print('__name__')
    
# util para importações 
    
if __name__ == '__main__':
    main()