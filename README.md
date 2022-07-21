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
2. Cada instância do servidor distribuído (uma por cruzamento) deve rodar em um processo paralelo em portas distintas) em cada uma das duas placas Raspberry Pi; 
4. Cada entrada / saída está representada na Tabela abaixo. Cada servidor distribuído é responsável pelo controle de um cruzamento.

<center> 

| Item                                              | GPIO Cruzamento 1 | GPIO Cruzamento 2 | Direção |
|---------------------------------------------------|:----:|:----:|:-------:|
| SEMAFORO_1_VERDE                                  |  01  | 02 | Saída   |
| SEMAFORO_1_AMARELO                                |  26  | 03 | Saída   |
| SEMAFORO_1_VERMELHO                               |  21  | 11 | Saída   |
| SEMAFORO_2_VERDE                                  |  20  |  0 | Saída   |
| SEMAFORO_2_AMARELO                                |  16  | 05 | Saída   |
| SEMAFORO_2_VERMELHO                               |  12  | 06 | Saída   |
| BOTAO_PEDESTRE_1                                  |  08  | 10 | Entrada |
| BOTAO_PEDESTRE_2                                  |  07  | 09 | Entrada |
| SENSOR_PASSAGEM_1                                 |  14  | 04 | Entrada |
| SENSOR_PASSAGEM_2                                 |  15  | 17 | Entrada |
| SENSOR_VELOCIDADE_1_A                             |  18  | 27 | Entrada |
| SENSOR_VELOCIDADE_1_B                             |  23  | 22 | Entrada |
| SENSOR_VELOCIDADE_2_A                             |  24  | 13 | Entrada |
| SENSOR_VELOCIDADE_2_B                             |  25  | 19 | Entrada |

</center> 

[Link do Dashboard - Cruzamento 1](http://164.41.98.25:8080/dashboard/0fe7b8e0-031e-11ed-9f25-414fbaf2b065?publicId=ba042a80-0322-11ed-9f25-414fbaf2b065)  
[Link do Dashboard - Cruzamento 2](http://164.41.98.25:8080/dashboard/d0680ee0-06d3-11ed-b55b-052a89b3b188?publicId=ba042a80-0322-11ed-9f25-414fbaf2b065)  
[Link do Dashboard - Cruzamento 3](http://164.41.98.25:8080/dashboard/35007810-06d4-11ed-b55b-052a89b3b188?publicId=ba042a80-0322-11ed-9f25-414fbaf2b065)  
[Link do Dashboard - Cruzamento 4](http://164.41.98.25:8080/dashboard/59bd6050-06d4-11ed-b55b-052a89b3b188?publicId=ba042a80-0322-11ed-9f25-414fbaf2b065)  


## 4. Requisitos

Os sistema de controle possui os seguintes requisitos:

### Servidores Distribuídos

O código do Servidor Distribuído deve ser desenvolvido em **Python**, **C** ou **C++**;  

Os servidores distribuídos tem as seguintes responsabilidades:  
1. Controlar os **semáforos** (temporização) - cruzamento com 4 sinais: os semáforos da via principal tem temporização diferente dos das vias auxiliares conforme e tabela abaixo.

<center> 

| Estado                                            | Via Principal (s) | Via Auxiliar (s) | 
|---------------------------------------------------|:----:|:---:|
| Verde (mínimo)                                    |  10  | 5   |
| Verde (máximo)                                    |  20  | 10  |
| Amarelo                                           |  03  | 03  |
| Vermelho (mínimo)                                 |   5  | 10  |
| Vermelho (máximo)                                 |  10  | 20  |
| Vermelho Total (Vemrlho em ambas as direções)     |  01  | 01  |

</center> 

2. Controlar o acionamento dos **botões de travessia** de pedestres (2 por cruzamento): ao acionar o botão, o sinal em questão deverá cumprir seu tempo mínimo (Ex: permanecer verde pelo tempo mínimo antes de fechar. Caso o tempo mínimo já tenha passado, o sinal irá mudar de estado imediatamente após o botão ser pressionado);
3. Controlar o acionamento dos **sensores de passagem de carros** nas vias auxiliares. Caso o sinal esteja fechado e um carro pare na via auxiliar, o comportamente será o mesmo que um pedestre pressionar o **botões de travessia**;
4. Contar a *passagem de carros* em cada direção e sentido do cruzamento (4 valores sepadados) e enviar esta informação periodicamente (2 segundos) ao servidor central;
5. Monitorar a velocidade da via através dos **sensores de velocidade**. A velocidade de cada carro deverá ser reportada para o servidor central periodicamente. Veídulos acima da velocidade permitida de 60 Km/h deverão ser reportados ao servidor central e contabilizados separadamente. Além disso, é necessário soar um alarme ao detectar um veículo acima da velocidade permitida;
6. Efetuar o controle de *avanço do sinal vermelho* tanto através dos **sensores de passagem de carros** nas vias auxiliares quanto pelos **sensores de velocidade** na via principal. O número de veículos que avançam o sinal vermelho deverá ser reportado ao servidor central e o alarme deve ser disparado a cada detecção de infração;
7. Cada instância dos servidores distribuídos a ser executada deve automaticamente se configurar para o controle do cruzamento 1 ou 2, seja por passagem de parâmetro de inicialização, arquivo de configuração ou outro mecanismo, ou seja, o programa que controla ambos os cruzamentos deverá ser um só.

### Servidor Central

O código do Servidor Central pode ser desenvolvido em **Python**, **C** ou **C++**. Em qualquer uma das linguagens devem haver instruções explicitas de como instalar e rodar. Para C/C++ basta o Makefile e incluir todas as dependências no próprio projeto.

O servidor central tem as seguintes responsabilidades:  
1. Manter conexão com os servidores distribuídos (TCP/IP);  
2. Prover uma **interface** que mantenham atualizadas as seguintes informações por cruzamento:  
    a. **Fluxo de trânsito** nas vias principais (Carros/min);    
    b. **Velocidade média da via** (km/h);   
    c. **Número de infrações** (Por tipo: avanço de sinal e velocidade acima da permitida);  
3. Prover **mecanismo na interface** para:  
    a. **Modo de emergência**: liberar o fluxo de trânsito em uma via (os dois cruzamentos com a via principal em verde);     
    b. **Modo noturno** fazer o sinal amarelo piscar em todos os cruzamento;  

### Geral

1. Os códigos em C/C++ devem possuir Makefile para compilação;
2. Cada serviço (programa) deve poder ser iniciado independente dos demais e ficar aguardando o acionamento dos demais;
3. Deverá haver um arquivo README no repositório descrevento o modo de instalação/execução e o modo de uso do programa.

## 5. Detalhes de Implementação

1. **Botão de travessia de pedestre**: devem tratar o *debounce*. No simulador, o sinal do botão é acionado por um intervalo de 300 a 400 ms. 
2. **Sensor de Velocidade**: estes sensores são implementados através do sensor de efeito hall. O sensor de velocidade é composto por dois sensores A e B onde o sensor A fica mais próximo do sinal de 
trânsito e o sensor B mais afastado. A distância entre os dois sensores é de 1 metro. Na passagem de um carro, o sensor B é acionado primeiro e depois o sensor A. Neste caso, para calcular a velocidade do carro passando pelos sensores, é necessário calcular o intervalo de tempo entre o acionamentdo do sensor B e do sensor A (Seja, nos dois casos, o evento de subida ou de descida) em seguida, dividir a distância entre os sensores (1 metro) pelo intervalo de tempo medido.  

## 6. Critérios de Avaliação

A avaliação será realizada seguindo os seguintes critérios: 

|   ITEM    |   DETALHE  |   VALOR   |
|-----------|------------|:---------:|
|**Servidor Central**    |       |       |
<!-- |**Interface (Monitoramento)**  |   Interface gráfica (via terminal, web, etc) apresentando o estado de cada dispositivo (entradas e saídas), a temperatura, umidade e o número de pessoas ocupando o prédio sendo atualizada periodicamente.  |   1,0   |
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
|**Pontuação Extra** |   Qualidade e usabilidade acima da média. |   0,5   |  -->

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
