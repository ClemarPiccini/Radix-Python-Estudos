https://www.youtube.com/watch?v=zDYL22QNiWk


Instalação do Pipenv

Se você ainda não tem o Pipenv instalado, pode instalar usando o pip:

```pip install pipenv```

Criando um novo projeto com Pipenv

Para criar um novo projeto e inicializar um ambiente virtual com o Pipenv, você pode fazer o seguinte:

Navegue até o diretório onde deseja criar o projeto.

Execute o comando pipenv --python 3.8 (substitua 3.8 pela versão do Python desejada) para criar um novo ambiente virtual usando o Python especificado.


cd meu_projeto

```pipenv --python 3.8```

Adicionando Dependências

Para adicionar dependências ao seu projeto e atualizar o arquivo Pipfile, você pode usar o comando pipenv install seguido pelo nome dos pacotes que deseja instalar. Por exemplo, para adicionar o pacote requests, você faria o seguinte:


```pipenv install requests```

Isso instalará o pacote requests e atualizará o arquivo Pipfile com a nova dependência.

Ativando o Ambiente Virtual

Para ativar o ambiente virtual do projeto e começar a trabalhar nele, você pode usar o comando pipenv shell:


```pipenv shell```

Isso ativará o ambiente virtual e ajustará as variáveis de ambiente para que o Python e outras ferramentas usem as dependências do projeto.

Executando Scripts Personalizados
Você pode definir scripts personalizados no arquivo Pipfile para realizar tarefas comuns, como iniciar o servidor de desenvolvimento. Por exemplo, se você tiver um script chamado start que inicia o servidor, você pode executá-lo usando o comando pipenv run:


```pipenv run start```

Isso executará o script start definido no Pipfile.
