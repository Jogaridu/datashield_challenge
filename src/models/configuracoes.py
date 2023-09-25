import os
import subprocess
import uuid
import sys


sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'database'))
from conexao_db  import instanciar_usuarios, instanciar_analise

colecao_usuarios = instanciar_usuarios()
colecao_analise = instanciar_analise()

caminho_arquivo = "src/config/config.json"

class Configuracoes:

    id = ""

    def __init__(self):
        self.id = self.pegar_uuid()

    def pegar_uuid(self):

        mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(2, -1, -1)])
        return str(uuid.uuid5(uuid.NAMESPACE_DNS, mac))


    def pegar_config(self):

        dados = colecao_usuarios.find_one({"uuid": self.id})
        del dados['_id']
        return dados


    def validar_config(self):

        dados = self.pegar_config()

        # Verificar se existe configuração, caso contrário, uma config será criada
        if dados == None:

            resultado = subprocess.check_output('whoami', shell=True)
            saidacmd = resultado.decode('utf-8').strip()

            saidacmd = saidacmd.split("\\")
            nomeUsuario = saidacmd[-1]

            # Criação dos dados iniciais
            dados_iniciais = {
                "status": "inativo",
                "nome_usuario": nomeUsuario,
                "processos_analisados": 0,
                "ultima_analise": "Sem análise",
                "uuid": self.id
            }

            colecao_usuarios.insert_one(dados_iniciais)
        
        return True


    def atualizar_config(self, novos_dados):

        colecao_usuarios.update_one({"uuid": self.id}, {'$set': novos_dados})
        

    def definir_processos_analisados(self):

        qtde = len(list(colecao_analise.find({"uuid": self.id})))
        self.atualizar_config({'processos_analisados': qtde})

        return qtde
    

    def definir_status(self, status):

        self.atualizar_config({'status': status})
        return True


    def definir_ultima_analise(self, data):

        self.atualizar_config({'ultima_analise': data})
        return True


obj_configuracoes = Configuracoes()