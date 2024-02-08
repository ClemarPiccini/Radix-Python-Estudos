# Abrindo um arquivo para leitura
with open('arquivo.txt', 'r') as file:
    # Lendo todo o conteúdo de uma vez
    content = file.read()
    print(content)

    # Lendo linha por linha
    file.seek(0)  # Voltando para o início do arquivo
    for line in file:
        print(line.strip())  # Strip remove espaços em branco extras, incluindo quebras de linha

# O arquivo é fechado automaticamente após o bloco 'with'

# Abrindo um arquivo para gravação
with open('arquivo.txt', 'w') as file:
    # Gravando conteúdo no arquivo
    file.write('Hello, world!\n')
    file.write('This is a new line.\n')

# O arquivo é fechado automaticamente após o bloco 'with'
