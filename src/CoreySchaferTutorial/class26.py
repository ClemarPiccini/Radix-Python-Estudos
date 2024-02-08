import os 
import re

# Diretório contendo os arquivos a serem renomeados
diretorio = '/caminho/do/seu/diretorio'

# Padrão para identificar os arquivos a serem renomeados
padrao = r'^arquivo(\d+)\.txt$'

# Loop pelos arquivos no diretório
for nome_arquivo in os.listdir(diretorio):
    caminho_completo = os.path.join(diretorio, nome_arquivo)
    if os.path.isfile(caminho_completo):
        # Verifica se o nome do arquivo corresponde ao padrão
        correspondencia = re.match(padrao, nome_arquivo)
        if correspondencia:
            # Extrai o número do arquivo
            numero = correspondencia.group(1)
            # Novo nome do arquivo
            novo_nome = f'novo_nome_{numero}.txt'
            novo_caminho_completo = os.path.join(diretorio, novo_nome)
            # Renomeia o arquivo
            os.rename(caminho_completo, novo_caminho_completo)
