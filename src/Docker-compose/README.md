https://www.youtube.com/watch?v=MVIcrmeV_6c

### Docker Compose é uma ferramenta que permite definir e executar aplicativos multi-contêineres. Com o Docker Compose, você pode usar um arquivo YAML para configurar os serviços do seu aplicativo, como bancos de dados, servidores da web, cache, etc., e depois iniciar todos os serviços com um único comando. Isso facilita o gerenciamento de aplicativos complexos que consistem em vários contêineres interconectados.

# Gerenciamento de aplicativos com Docker Compose:

docker-compose up: Inicia todos os serviços definidos no arquivo docker-compose.yml.
docker-compose up -d: Inicia todos os serviços em segundo plano (detached mode).
docker-compose down: Para e remove todos os contêineres, redes e volumes associados ao aplicativo.
docker-compose ps: Lista os serviços em execução.

# Gerenciamento de serviços individuais:

docker-compose start <service_name>: Inicia um serviço específico.
docker-compose stop <service_name>: Para um serviço específico.
docker-compose restart <service_name>: Reinicia um serviço específico.
docker-compose logs <service_name>: Exibe os logs de um serviço específico.

# Outros comandos úteis:

docker-compose build: Constrói ou reconstrói os serviços.
docker-compose config: Valida e exibe a configuração do arquivo docker-compose.yml.
docker-compose exec <service_name> <command>: Executa um comando dentro de um serviço.