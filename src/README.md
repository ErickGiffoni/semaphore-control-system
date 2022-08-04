### Como executar

Python 3.10.5

- entrar na pasta src
- editar o arquivo ./utils/config.json com o ip da máquina e portas
- python3 -m central.central N\_DISTRIBUTED
- python3 -m distributed.distributed DISTRIBUTED\_ID

N\_DISTRIBUTED é o número de distribuídos que vão existir (mínimo é 1 e o máximo é 4).
DISTRIBUTED\_ID é o ID do servidor distribuído (mínimo é 1 e o máximo é 4).

Exemplo:

- python3 -m central.central 3
- python3 -m distributed.distributed 1
- python3 -m distributed.distributed 2
- python3 -m distributed.distributed 3


### Limitações conhecidas

- O arquivo ./utils/config.json precisa ser editado antes de executar os comandos. Se ele for editado após subir o servidor central, ele bloqueia conexões diferentes de quando ele leu o arquivo.
- O botão de pedestre funciona, mas a sincronia dos semáforos é perdida.
- Não foi implementado buzzer, modo de emergência, modo noturno e interface no central.

### Recursos

- https://docs.python.org/3/library/socket.html
- https://docs.python.org/3/library/signal.html
- https://docs.python.org/3/library/threading.html
- https://www.freecodecamp.org/portuguese/news/ler-arquivos-json-em-python-como-usar-load-loads-e-dump-dumps-com-arquivos-json/
- https://www.geeksforgeeks.org/socket-programming-python/
- https://yasoob.me/2013/08/06/python-socket-network-programming/
- https://www.tutorialspoint.com/python3/python_multithreading.htm
