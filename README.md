# DataShield - Challenge 2023

## PT-BR

## Introdução
Challenge realizado com o intuito de colocar em prática todos os conhecimentos aprendidos durante o primeiro ano do curso de Defesa Cibernética, incluindo programação, sistemas operacionais, e análise de malwares. 

# Integrantes
- Eduardo dos Santos Almeida
- Jorge Gabriel Ricci Dutra
- Matheus Rosa Colombo
- Pedro Augusto Buhrer Pereira
  
## Desafio
O desafio consiste em desenvolver um software capaz de detectar e mitigar um ransomware de mercado que será desenvolvido pela empresa parceira PRIDE Security. Alem disso devemos criar uma startup com nome, identidade, logo, etc.  

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


# DataShield - Challenge 2023

## EN-US

## Introduction
Challenge carried out with the objective of putting into practice all the knowledge learned during the first year of the Cyber Defense course, including programming, operating systems, and malware analysis. 

# Members
- Eduardo dos Santos Almeida
- Jorge Gabriel Ricci Dutra
- Matheus Rosa Colombo
- Pedro Augusto Buhrer Pereira
  
## Challenge
The challenge is to develop software capable of detecting and mitigating market ransomware that will be developed by partner company PRIDE Security. Furthermore, we must create a startup with a name, identity, logo, etc.  

We carried out in-depth research on the subject, which taught us what a malware detector needed and what strategies we should use. We developed an application with a graphical interface, a website to download our tool, and created a sanbox environment for testing using a Windows 10 virtual machine.

## What are Ransomware?
ransomware is a type of malware as well as viruses, worms, spyware and trojans.

When ransomware gains access to the device, it encrypts the entire operating system or just individual files and then a ransom is demanded from the victims, normally a large amount is requested and in cryptocurrencies.

According to Forbes, in 2021, 80% of organizations were hit by a ransomware attack.

## A Datashield

### Renewing what already exists with fresh ideas

Based on this challenge, Datashield was invented and worked on throughout the year with the objective of carrying out and solving the challenge in an impeccable way.

### Protect your data, preserve your memorable stories

## Pillars and Architecture

Project combines a WEB interface based on the MVC (Model-View-Controller) architecture with the use of the Flask framework with a cloud database.
- Machine Learning
- Honeypot
- Process analysis and monitoring
- Monitoring Windows event logs

## Step by step to run the program

### 1° Step - Open the terminal

### 2° Step - Get the project from github
To obtain the files, type the command: 
```
git clone (https://github.com/Jogaridu/datashield_challenge)
cd datashield_challenge
```
### 3° Step - Install the libraries

```
pip install libraryname
```

#### List of libraries to be installed:
Name   | Description
:------: | :-----------:
ctypes | Library used to make function calls in shared libraries (DLLs) written in C and to define C data types in Python.
signal | Library used to manipulate system signals, such as process interruptions, allowing control of behavior in specific situations.
datetime | Library used to work with dates and times, allowing the creation, manipulation and formatting of date and time objects.
socket | Library used for network communication, allowing the creation of sockets to establish connections between processes on different machines.
flask | Python web framework used to build web applications, offering tools to create RESTful APIs and simple web applications.
subprocess | Library used to create, manage and interact with secondary processes from a Python program.
json | Library used to encode and decode data in JSON format, commonly used for data interoperability.
sys | Library that provides access to system-specific functionality, such as command-line arguments and information about the version of Python running.
livereload | Used to create a development server that automatically reloads the browser when source files are modified.
time | Library that provides functions to measure time and delay code execution.
locale | Library used for internationalization and localization of applications, allowing the formatting of numbers, dates and currencies according to regional settings.
urllib.parse | Used to parse URLs and perform URL-related operations, such as constructing queries.
os | Library that provides functions for interacting with the operating system, such as manipulating directories, executing commands, and checking files.
uuid | Library used to generate universally unique identifiers (UUIDs).
psutil | Library that allows you to obtain system information, such as information about running processes, CPU and memory usage.
webview | Used to create web-based graphical user interfaces embedded in desktop applications.
pymongo | Python driver for MongoDB, allowing interaction with MongoDB databases from Python code.
winshell | Used to interact with the Windows desktop environment, allowing operations such as creating shortcuts.
pythoncom | Used to interact with the COM (Component Object Model) infrastructure on Windows systems.
win32con | Provides Windows system constants for use in API calls.
server | It is not a recognized standard Python library. It may be specific to a particular project or application.
wmi | Used to interact with Windows Management Instrumentation (WMI), allowing access to Windows system information and settings.

### 4° Step – Run the command below to open the Python program
```
python main.py ou python3 main.py
```
### 5° Step - Turn on endpoint monitoring

<img src="https://datashield.avalontech.net.br/static/assets/images/interface.png" />

### Ransomware testing environment
Operating system: Windows 10 <br>
Processor: Intel Pentium G4560 3.5Ghz <br>
RAM: 4GB <br>
SSD: 128GB <br>
