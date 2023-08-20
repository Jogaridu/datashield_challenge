import os
import json
import subprocess

caminho_arquivo = "src/config/config"

def validar_arquivo_config():

    global caminho_arquivo

    # Verificar se o arquivo existe, caso contrário, criá-lo
    if not os.path.exists(caminho_arquivo):

        resultado = subprocess.check_output('whoami', shell=True)
        saidacmd = resultado.decode('utf-8').strip()

        saidacmd = saidacmd.split("\\")
        nomeUsuario = saidacmd[-1]

        # Criação dos dados iniciais
        dados_iniciais = {
            "status": "inativo",
            "nome_usuario": nomeUsuario,
            "processos_analisados": 100,
            "ultima_analise": "2023-08-20"
        }

        # Criação do arquivo de configuração
        with open(caminho_arquivo, "w") as arquivo:
            json.dump(dados_iniciais, arquivo, indent=4)
        
    return True


def atualizar_arquivo_config(novos_dados):

    global caminho_arquivo

    # Ler os dados existentes do arquivo
    with open(caminho_arquivo, "r") as arquivo:
        dados_existentes = json.load(arquivo)

    # Atualizar os dados existentes com os novos dados
    dados_existentes.update(novos_dados)

    # Escrever os dados atualizados de volta para o arquivo
    with open(caminho_arquivo, "w") as arquivo:
        json.dump(dados_existentes, arquivo, indent=4)
    


def pegar_config():

    global caminho_arquivo

    # Ler os dados do arquivo de configuração
    with open(caminho_arquivo, "r") as arquivo:
        dados = json.load(arquivo)
        return dados
