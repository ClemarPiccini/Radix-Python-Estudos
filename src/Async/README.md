https://www.youtube.com/watch?v=GpqAQxH1Afc  

Em Python, async e await são utilizados para programação assíncrona, que é uma forma de escrever código que pode lidar com operações que podem ser executadas de forma independente, como requisições de rede, leitura e escrita de arquivos, entre outras, sem bloquear o fluxo principal do programa.  

async: É usado para declarar uma função assíncrona. Isso significa que a função pode ser pausada e retomada mais tarde, permitindo que outras partes do código sejam executadas enquanto ela aguarda o resultado de uma operação assíncrona.  

await: É usado dentro de uma função assíncrona para esperar que uma outra função assíncrona termine e retorne um resultado. Quando você usa await, o Python pausa a execução da função assíncrona atual até que a função chamada seja concluída. Durante esse tempo de espera, o controle é devolvido ao loop de eventos para que outras tarefas assíncronas possam ser executadas.  
