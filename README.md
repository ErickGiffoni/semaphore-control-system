# Trabalho 1 (2022-1)

Trabalho 1 da disciplina de Fundamentos de Sistemas Embarcados (2022/1)

## 1. Objetivos

Este trabalho tem por objetivo a criação de um sistema distribuído para o controle e monitoramento de um grupo de sinais de trânsito. O sistema deve ser desenvolvido para funcionar em um conjunto de placas Raspberry Pi com um ***servidor central*** responsável pelo controle e interface com o usuário e ***servidores distribuídos*** para o controle local e monitoramento dos sinais do cruzamento junto aos respectivos sensores que monitoram as vias. Dentre os dispositivos envolvidos estão o controle de temporizaçãio e acionamento dos sinais de trânsito, o acionmento de botões de passagens de pedestres, o monitoramento de sensores de passagem de carros bem como a velocidade da via e o avanço de sinal vermelho.

A Figura 1 mostra o layout dos cruzamentos.

![Figura](/figuras/Cruzamentos.png)

Cada cruzamento possui:
- 4 Sinais de Trânsito (Em pares);
- 2 botões de acionamento para pedestres (pedir passagem);
- 2 Sensores de presença/passagem de carros (nas vias auxiliares, um em cada direção);
- 2 Sensores de velocidade/presença/passagem de carros (nas vias principais, um em cada direção);
- 1 Sinalização de áudio (buzzer) para sinalizar quando o sinal está mudando de estado (quando o cruzamento de pedestres irá ser fechado);

Cada cruzamento deverá ser controlado por um processo indivisual que esteja rodando em uma placa Raspberry Pi e cada controlador de cruzamento deve se comunicar via rede (TCP/IP) com o servidor central.

Na Figura 2 é possível ver a arquitetura do sistema.

![Figura](/figuras/arquitetura_trabalho_1.png)


Requisitos:
Serviços distribuídos: 1 processo por cruzamento;
Serviço central: controle centralizado do sistema;

Requisitos dos Serviços Distribuídos:
Controle de semáforos (temporização) - cruzamento com 4 sinais;
Controle de interrupções (pedestres) - botão de travessia 
Contagem de carros por uma via (sensor)
Controle de velocidade na via (sensores sequenciais) cálculo da velocidade pelo intervalo de tempo entre acionamento dos sensores.
Sincronia de mais de 1 módulo (TCP/IP)
Alarme ao detectar um veículo acima da velocidade
Detecção de veículos cruzando o sinal vermelho
Contagem de fluxo de tráfego na via
Comunicação do estado ao servidor central (Envio de estado e recepção de comandos)

Requisitos do Servidor Central:
Display do estado do trânsito;
Recepção e envio de comandos gerais (emergência, fluxo, etc)

## 2. Componentes do Sistema

Para simplificar a implementação e logística de testes do trabalho, a quantidade de cruzamentos será limitada a 4 sendo que haverão 2 placas Raspberry Pi, cada uma dedicada a rodar os serviços de controle de 2 cruzamentos e uma terceira placa Raspberry Pi para rodar o servidor Central. 

### O sistema do Servidor Central será composto por:
1. 01 Placa Raspberry Pi 4;

### Cada unidade dos Servidores Distribuídos será composto por:
1. 01 Placa Raspberry Pi 4;
2. 12 Saídas (LEDs) representando os semáforos;
3. 04 Entradas sendo os botões de pedestre;
4. 04 Entradas sendo os sensores de presença/contagem de veículos das vias auxiliares (2 por cruzamento);
5. 08 Entradas sendo os sensores de velocidade/presença/contagem (4 por cruzamento);
6. Saída de áudio para efeito sonoro estado do sinal para deficientes auditivos;

## 3. Conexões entre os módulos do sistema

1. Os servidores distribuídos deverão se comunicar com o servidor central através do Protocolo TCP/IP (O formato das mensagens ficam à cargo do aluno. A sugestão é o uso do formato JSON);
2. Cada instância do servidor distribuído (uma por cruzamento) deve rodar em um processo paralelo em portas distintas); 
4. Cada entrada / saída está representada na Tabela abaixo.

| Item                                              | GPIO | Direção |
|---------------------------------------------------|:----:|:-------:|
| ***Cruzamento 1***                                |      |         |
| SEMAFORO_1_VERDE                                  |  01  | Saída   |
| SEMAFORO_1_AMARELO                                |  26  | Saída   |
| SEMAFORO_1_VERMELHO                               |  21  | Saída   |
| SEMAFORO_2_VERDE                                  |  20  | Saída   |
| SEMAFORO_2_AMARELO                                |  16  | Saída   |
| SEMAFORO_2_VERMELHO                               |  12  | Saída   |
| BOTAO_PEDESTRE_1                                  |  08  | Entrada |
| BOTAO_PEDESTRE_2                                  |  07  | Entrada |
| SENSOR_PASSAGEM_1                                 |  14  | Entrada |
| SENSOR_PASSAGEM_2                                 |  15  | Entrada |
| SENSOR_VELOCIDADE_1_A                             |  18  | Entrada |
| SENSOR_VELOCIDADE_1_B                             |  23  | Entrada |
| SENSOR_VELOCIDADE_2_A                             |  24  | Entrada |
| SENSOR_VELOCIDADE_2_B                             |  25  | Entrada |
| ***Cruzamento 2***                                |      |         |
| SEMAFORO_1_VERDE                                  |  02  | Saída   |
| SEMAFORO_1_AMARELO                                |  03  | Saída   |
| SEMAFORO_1_VERMELHO                               |  04  | Saída   |
| SEMAFORO_2_VERDE                                  |  17  | Saída   |
| SEMAFORO_2_AMARELO                                |  27  | Saída   |
| SEMAFORO_2_VERMELHO                               |  22  | Saída   |
| BOTAO_PEDESTRE_1                                  |  10  | Entrada |
| BOTAO_PEDESTRE_2                                  |  09  | Entrada |
| SENSOR_PASSAGEM_1                                 |  11  | Entrada |
| SENSOR_PASSAGEM_2                                 |  00  | Entrada |
| SENSOR_VELOCIDADE_1_A                             |  05  | Entrada |
| SENSOR_VELOCIDADE_1_B                             |  06  | Entrada |
| SENSOR_VELOCIDADE_2_A                             |  13  | Entrada |
| SENSOR_VELOCIDADE_2_B                             |  19  | Entrada |


Link do Dashboard (Sala de Aula): http://192.168.35.17:8080/dashboard/0fe7b8e0-031e-11ed-9f25-414fbaf2b065?publicId=ba042a80-0322-11ed-9f25-414fbaf2b065

<!-- ## 4. Requisitos

Os sistema de controle possui os seguintes requisitos:

### Servidor Central

O código do Servidor Central pode ser desenvolvido em **Python**, **C** ou **C++**. Em qualquer uma das linguagens devem haver instruções explicitas de como instalar e rodar. Para C/C++ basta o Makefile e incluir todas as dependências no próprio projeto.

O servidor central tem as seguintes responsabilidades:  
1. Manter conexão com os servidores distribuídos (TCP/IP);  
2. Prover uma **interface** que mantenham atualizadas as seguintes informações:  
    a. **Estado das entradas** (Sensores);  
    b. **Estado das Saídas** (lâmpadas, aparelhos de ar, etc.);   
    c. **Valor da temperatura e umidade** de cada andar a cada 1 segundo;  
    d. **Contador de Ocupação** (Número de Pessoas) presentes no prédio como um todo e um contador específico por andar (Serão 3 contadores separados);  
3. Prover **mecanismo na interface** para:  
    a. Acionar manualmente lâmpadas e aparelhos de ar-condicionado;   
    b. **Acionamento de uma alarme** que, quando estiver ligado, deve tocar um som de alerta ao detectar presenças ou abertura de portas/janelas;  
    c. **Acionamento de alarme de incêncio** que, ao detectar presença de fumaça a qualaquer momento deve soar o alarme e acionar os aspersores de incêndio;
4. Manter **log** (em arqvuio CSV) dos comandos acionados pelos usuários e do acionamento dos alarmes com data e hora e cada evento;  

### Servidores Distribuídos

O código do Servidor Distribuído deve ser desenvolvido em **Python**, **C** ou **C++**;  

Os servidores distribuídos tem as seguintes responsabilidades:  
1. Manter os valores de **temperatura e umidade** atualizados a cada 1 segundo (Sendo requisitado pelo servidor central periodicamente ou enviado via mensagem *push*);  
2. Acionar **Lâmpadas, aparelhos de Ar-Condicionado e os Aspersores de Incêndio** (mantendo informação sobre seu estado) conforme comandos do Servidor Central e retornando uma mensagem de confirmação para o mesmo sobre o sucesso ou não do acionamento;  
3. Manter o estado dos **sensores de presença e abertura de portas/janelas** informando ao servidor central imediatamente (*mensagem push*) quando detectar o acionamento de qualquer um deles;  
4. Manter o estado dos **sensores de fumaça** informando ao servidor central imediatamente (*mensagem push*) quando detectar o acionamento de qualquer um deles;  
5. Efetuar a contagem de pessoas entrando e saindo do prédio e de cada andar para controle de ocupação;
6. Cada instância dos servidores distribuídos deve ser iniciada conforme o arquivo descrição JSON disponível neste repositório (Somente a porta local de cada servidor deve ser modificada no arquivo para cada aluno conforme a distribuição de portas disponibilizada para a turma).

### Geral

1. Os códigos em C/C++ devem possuir Makefile para compilação;
2. Cada serviço (programa) deve poder ser iniciado independente dos demais e ficar aguardando o acionamento dos demais;
3. Deverá haver um arquivo README no repositório descrevento o modo de instalação/execução e o modo de uso do programa.

## 5. Detalhes de Implementação

1. Os sensores de contagem de pessoas serão acionados por aprox. 200 ms (podendo variar em aprox. 100 ms para mais ou para menos). Neste caso, o sistema deverá detectar e contar corretamente somente uma entrada ou saída.
2. O programa não poderá usar 100% da CPU em nenhum caso. Todas as threads/processos deverão funcionar com algum tipo de temporizador ou sleep para desocupar o processador em algum momento ou através de chamadas blocantes.
3. O programa do Servidor Distribuído deve ser genérico para poder ser associado a qualquer andar do prédio e inicializado à partir de um arquivo de configuração (JSON), disponível neste repositório.
4. Os sensores de presença nos corredores terão duas funções:  
   a. Caso o alarme esteja ligado, deverão acionar o alarme;  
   b. Caso o alrme esteja desligado, deverão acender a lâmpada do respectivo corredor por 15 segundos e depois apagar;
5. Deve haver um meio de ligar e desligar todas as cargas do prédio ou por andar. Neste caso são 6 comandos. (Liga/Desliga todo o prédio e Liga/Desliga todas as cargas -- Lampadas e aparelhos de Ar-Condicionado -- de um determinado andar).
6. Ao acionar o alarme, deve haver uma verificação se o sensores que ativam o alarme estão ligados. Neste caso, o sistema deve alertar o usuário e não permitir o acionamento do alarme enquanto todos os itens que o acionam estejam desativados.

## 6. Critérios de Avaliação

A avaliação será realizada seguindo os seguintes critérios: -->

<!-- |   ITEM    |   DETALHE  |   VALOR   |
|-----------|------------|:---------:|
|**Servidor Central**    |       |       |
|**Interface (Monitoramento)**  |   Interface gráfica (via terminal, web, etc) apresentando o estado de cada dispositivo (entradas e saídas), a temperatura, umidade e o número de pessoas ocupando o prédio sendo atualizada periodicamente.  |   1,0   |
|**Interface (Acionamento de Dispositivos)** |   Mecanismo para acionamento de lâmpadas e aparelhos de ar-condicionado individualmente ou em grupos. |   1,0   |
|**Acionamento do Alarme**   |   Mecanismo de ligar/desligar alarme e acionamento do alarme de acordo com o estado dos sensores com alerta no acionamento. |   0,5   |
|**Alarme de Incêndio**   |   Implementação da rotina de acionamento do alarme de incêncio com o correto acionamento dos aspersores. |   0,5   |
|**Log (CSV)**   |   Geração de Log em arquivo CSV.  |   0,5 |
|**Servidores Distribuídos**    |       |       |
|**Inicialização (Arquivo de Configuração)**    |   Correta inicialização do serviço à partir do arquivo de configuração JSON.  |   0,5   |
|**Leitura de Temperatura / Umidade**    |   Leitura, armazenamento e envio dos valores de temperatura / umidade por andar.  |   0,7   |
|**Acionamento de Dispositivos** |   Correto acionamento de lâmpadas, aparelhos de ar-condicionado e aspersor pelo comando do Servidor Central.    |   0,7   |
|**Estado dos Sensores** |   Correta leitura e envio (*mensagem push*) para o Servidor Central um alerta pelo acionamento dos sensores de presença / abertura de portas/janelas e sensor de fumaça.   |   0,8  |
|**Contagem de pessoas** |   Correta leitura dos sensores de contagem de pessoas (Por andar e Total).   |   0,8  |
|**Geral**    |       |       |
|**Comunicação TCP/IP**  |   Correta implementação de comunicação entre os servidores usando o protocolo TCP/IP, incluindo as mensagens do tipo *push*. |   1,5   |
|**Qualidade do Código / Execução** |   Utilização de boas práticas como o uso de bons nomes, modularização e organização em geral, bom desempenho da aplicação sem muito uso da CPU. |  1,5 |
|**Pontuação Extra** |   Qualidade e usabilidade acima da média. |   0,5   | -->

## 7. Referências

### Bibliotecas em Python

- gpiozero (https://gpiozero.readthedocs.io)
- RPi.GPIO (https://pypi.org/project/RPi.GPIO/)

A documentação da RPi.GPIO se encontra em
https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/

### Bibliotecas em C/C++

- WiringPi (http://wiringpi.com/)
- BCM2835 (http://www.airspayce.com/mikem/bcm2835/)
- PiGPIO (http://abyz.me.uk/rpi/pigpio/index.html)
- sysfs (https://elinux.org/RPi_GPIO_Code_Samples)

### Lista de Exemplos

Há um compilado de exemplos de acesso à GPIO em várias linguages de programação como C, C#, Ruby, Perl, Python, Java e Shell (https://elinux.org/RPi_GPIO_Code_Samples).
