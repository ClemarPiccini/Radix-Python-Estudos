https://www.youtube.com/watch?v=SORiTsvnU28


## CODIGO PARA INICIAR O SERVIDOR  

# tem que estar dentro do diretorio correto do arquivo main.py  

+``` python -m uvicorn main:app --reload ```


O FastAPI é um framework moderno de desenvolvimento web para Python. Ele é projetado para ser fácil de usar, rápido para desenvolver e capaz de lidar com cargas de trabalho intensas. Aqui estão algumas características principais do FastAPI:

Rápido Desenvolvimento: O FastAPI utiliza a abordagem de anotações de tipos do Python para definir os tipos de dados das requisições e respostas da API, o que torna a escrita do código mais rápida e menos propensa a erros.

Baseado em Padrões Abertos: O FastAPI é baseado em padrões abertos como o OpenAPI (anteriormente conhecido como Swagger), o que facilita a documentação automática da API e a interoperabilidade com outras ferramentas compatíveis com OpenAPI.

Suporte a Assíncrono: O FastAPI é construído sobre o framework Starlette, que é assíncrono por natureza. Isso significa que ele pode lidar com operações de entrada e saída de forma eficiente, especialmente em situações onde a concorrência é importante, como em APIs de alto tráfego.

Integração com Pydantic: O FastAPI possui integração nativa com o Pydantic, que é uma biblioteca para validação de dados com suporte a tipos de dados nativos do Python, como dicts, lists, tuples, etc. Isso facilita a validação dos dados de entrada e saída da API.

Suporte a WebSockets: Além de suportar requisições HTTP tradicionais, o FastAPI também oferece suporte a WebSockets, o que permite a criação de APIs em tempo real e aplicações que exigem comunicação bidirecional entre o cliente e o servidor.

Integração com outros Frameworks: O FastAPI pode ser facilmente integrado com outros frameworks e bibliotecas do ecossistema Python, como o SQLAlchemy para acesso a bancos de dados SQL ou o MongoDB para acesso a bancos de dados NoSQL.