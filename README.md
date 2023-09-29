# DataShield - Challenge 2023

## Repositório em EN-US
[Link para o GitHub]

## Introdução
Challenge realizado com o intuito de colocar em prática todos os conhecimentos aprendidos durante o primeiro ano do curso de Defesa Cibernética, incluindo programação, sistemas operacionais, e análise de malwares. 

# Integrantes
- Eduardo dos Santos Almeida
- Jorge Gabriel Ricci Dutra
- Matheus Rosa Colombo
- Pedro Augusto Buhrer Pereira
  
## Desafio
O desafio consiste em desenvolver um software capaz de detectar e mitigar um ransomware de mercado que será desenvolvido pela empresa parceira Fortinet. Alem disso devemos criar uma startup com nome, identidade, logo, etc.  

Realizamos uma pesquisa aprofundada no assunto, na qual nos ensinou o que um detector de malwares precisava e quais estrategias deveriamos utilizar. Desenvolvemos uma aplicação com interface gráfica, um site para download de nossa ferramenta, e a criação de um ambiente sanbox para teste usando uma maquina virtual Windows 10.

## O que são Ransomwares?

Os ransomwares se emcaixam dentro da categoria de malwares assim como virus, worms, spywares e trojans.

Os ransomwares ao ganhar acesso ao dispositivo, encriptam todo o sistema operacional ou apenas arquivos individuais e um resgate é exigido das vítimas em questão, normalmente sao requisitados um valor alto e em criptomoedas.

Segundo a Forbes, em 2021, 80% das organizações foram atingidas por um ataque de ransomware.

## A Datashield

### Renovando o que já existe com ideias frescas

A partir desse desafio, a Datashield foi inventada e trabalhada durante o ano todo com o intuito de realizar e resolver o desafio de uma maneira impecável.

### Proteja seus dados, conserve suas histórias memoráveis

## Pilares e Arquitetura

Projeto combina uma interface WEB baseada na arquitetura MVC (Model-View-Controller) com o uso do framework Flask com banco de dados em nuvem.

- Machine Learning
- Honeypot
- Análise e monitoramento de processos 
- Monitoramento dos logs de eventos do Windows

## Passo a passo para executar o programa

### 1° Passo - Abrir o terminal

### 2° Passo - Obter o projeto do github
Para obter os arquivos digite o comando: 
```
git clone (https://github.com/Jogaridu/datashield_challenge)
cd datashield_challenge
```
### 3° Passo - Instale as bibliotecas

```
pip install nomedabiblioteca
```

#### Lista de bibliotecas para serem instaladas: 
Nome   | Descrição
:------: | :-----------:
ctypes | Biblioteca usada para fazer chamadas de funções em bibliotecas compartilhadas (DLLs) escritas em C e para definir tipos de dados C em Python.
signal | Biblioteca usada para manipular sinais do sistema, como interrupções de processo, permitindo o controle de comportamentos em situações específicas.
datetime | Biblioteca usada para trabalhar com datas e horas, permitindo a criação, manipulação e formatação de objetos de data e hora.
socket | Biblioteca usada para comunicação de rede, permitindo a criação de sockets para estabelecer conexões entre processos em diferentes máquinas.
flask | Framework web em Python usado para construir aplicativos web, oferecendo ferramentas para criar APIs RESTful e aplicativos web simples.
subprocess | Biblioteca usada para criar, gerenciar e interagir com processos secundários a partir de um programa Python.
json | Biblioteca usada para codificar e decodificar dados no formato JSON, comumente usado para interoperabilidade de dados.
sys | Biblioteca que fornece acesso a funcionalidades específicas do sistema, como argumentos da linha de comando e informações sobre a versão do Python em execução.
livereload | Usado para criar um servidor de desenvolvimento que recarrega automaticamente o navegador quando os arquivos de origem são modificados.
time | Biblioteca que fornece funções para medir o tempo e atrasar a execução de código.
locale | Biblioteca usada para internacionalização e localização de aplicativos, permitindo a formatação de números, datas e moedas de acordo com as configurações regionais.
urllib.parse | Usada para analisar URLs e realizar operações relacionadas a URL, como a construção de consultas.
os | Biblioteca que fornece funções para interagir com o sistema operacional, como manipulação de diretórios, execução de comandos e verificação de arquivos.
uuid | Biblioteca usada para gerar identificadores únicos universalmente (UUIDs).
psutil | Biblioteca que permite a obtenção de informações do sistema, como informações sobre processos em execução, uso de CPU e memória.
webview | Usado para criar interfaces gráficas de usuário baseadas em web incorporadas em aplicativos de desktop.
pymongo | Driver Python para o MongoDB, permitindo a interação com bancos de dados MongoDB a partir de código Python.
winshell | Usada para interagir com o ambiente de desktop do Windows, permitindo operações como criar atalhos.
pythoncom | Usada para interagir com a infraestrutura COM (Component Object Model) em sistemas Windows.
win32con | Fornece constantes do sistema Windows para uso em chamadas de API.
server | Não é uma biblioteca Python padrão reconhecida. Pode ser específica para um projeto ou aplicativo em particular.
wmi | Usada para interagir com o Windows Management Instrumentation (WMI), permitindo acesso a informações e configurações do sistema Windows.

### 4° Passo - Execute o comando abaixo para abrir o programa Python
```
python main.py ou python3 main.py
```
### 5° Passo - Ligar monitoramento do endpoint

<img src="https://datashield.avalontech.net.br/static/assets/images/interface.png" />

### Ambiente de teste de ransomwares
Sistema operacional: Windows 10 <br>
Processador: Intel Pentium G4560 3.5Ghz <br>
RAM: 4GB <br>
SSD: 128GB <br>
