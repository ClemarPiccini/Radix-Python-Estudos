### MODULE os ###

import os

# Criar um diretório
os.mkdir('novo_diretorio')

# Listar arquivos em um diretório
arquivos = os.listdir('caminho_do_diretorio')

# Renomear um arquivo
os.rename('antigo_nome.txt', 'novo_nome.txt')

# Excluir um arquivo
os.remove('arquivo_para_excluir.txt')

# Excluir um diretório vazio
os.rmdir('diretorio_para_excluir')

# Obter o diretório atual
diretorio_atual = os.getcwd()

# Alterar o diretório atual
os.chdir('novo_diretorio')

# Verificar se um caminho existe
existe = os.path.exists('caminho_do_arquivo')

# Verificar se é um diretório
e_diretorio = os.path.isdir('caminho_do_diretorio')

# Verificar se é um arquivo
e_arquivo = os.path.isfile('caminho_do_arquivo')

# Obter valor de uma variável de ambiente
valor = os.getenv('NOME_DA_VARIAVEL')

# Definir uma nova variável de ambiente
os.environ['NOVA_VARIAVEL'] = 'valor'

# Executar um comando do sistema
os.system('ls -l')

# Juntar caminhos de diretório
caminho_completo = os.path.join('diretorio', 'subdiretorio', 'arquivo.txt')

# Separar o nome do arquivo do caminho
nome_arquivo = os.path.basename(caminho_completo)

# Obter o diretório pai
diretorio_pai = os.path.dirname(caminho_completo)

# Separar o nome do arquivo e a extensão
nome_arquivo, extensao = os.path.splitext(nome_arquivo)
