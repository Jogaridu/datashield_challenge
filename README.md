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

A partir desse desafio, a Datashield foi inventada e trabalhada durante o ano todo com o intuito de realizar e resolver o desafio de uma maneira impecavel.

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

### 4° Passo - Execute o comando abaixo para abrir o programa Python
```
python main.py ou python3 main.py
```
### 5° Passo - Ligar monitoramento do endpoint 
<img src="C:\Área de Trabalho\honeypot_monitor\datashield_challenge\src\static\assets\images\imagem-interface.png">

### Lista de bibliotecas a serem instaladas: 

- ctypes                                           - signal
- datetime                                         - socket
- flask                                            - subprocess
- json                                             - sys
- livereload                                       - time
- locale                                           - urllib.parse 
- os                                               - uuid
- psutil                                           - webview
- pymongo                                          - winshell
- pythoncom                                        - win32con
- server                                           - wmi

### Ambiente de teste de ransomwares
Sistema operacional: Windows 10
Processador: Intel Pentium G4560 3.5Ghz
RAM: 4GB
SSD: 128GB
