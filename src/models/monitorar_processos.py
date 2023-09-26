import psutil  
import os, signal
import wmi
import sys
import time
import json
import uuid

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from sklearn import tree

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'database'))
from conexao_db  import instanciar_processos, instanciar_analise
import models.honeypot as honeypot

# Instância do banco
colecao_processos = instanciar_processos() # Resultado
colecao_analise = instanciar_analise() # Dados de análise de novo processo

# Régua para uso de dados
# MAX_HANDLE_COUNT = 1000
# MAX_PAGE_FAULTS = 52000
# MAX_PAGE_FILE_USAGE = 90000
# MAX_PEAK_PAGE_FILE_USAGE = 110000
# MAX_WORKING_SET_SIZE = 105243072
# MAX_THREAD_COUNT = 35
# MAX_PRIORITY = 12
# MAX_PRIVATE_PAGE_COUNT = 70000000
MAX_HANDLE_COUNT = 1000
MAX_PAGE_FAULTS = 52000
MAX_PAGE_FILE_USAGE = 201048064
MAX_PEAK_PAGE_FILE_USAGE = 201048064
MAX_WORKING_SET_SIZE = 150242880
MAX_THREAD_COUNT = 20
MAX_PRIORITY = 12
MAX_PRIVATE_PAGE_COUNT = 70000000

class EventoHoneypotHandler(FileSystemEventHandler):

    def __init__(self):
        self.pasta_modificada = False
    
    def on_any_event(self, event):
        self.pasta_modificada = True
        # win32evtlogutil.ReportEvent("Datashield", 1000, eventCategory=0, eventType=win32con.EVENTLOG_WARNING_TYPE, strings=['Atividade maliciosa'])
        print("Foi identificado uma mudança na pasta: " + event.src_path)


class Monitoramento:

    # UUID
    id = ''

    # Machine learning
    classif =  tree.DecisionTreeClassifier()

    # Honeypot
    evento_handler = EventoHoneypotHandler()
    id = ''

    def __init__(self):
        self.monitoramento_ativo = False
        self.id = self.pegar_uuid()


    def status(self):
        return self.monitoramento_ativo


    def parar(self):
        self.monitoramento_ativo = False

 
    def iniciar(self):

        self.machine_learning_iniciar()

        self.monitoramento_ativo = True

        self.c = wmi.WMI(privileges=["Security"])
        self.process_watcher = self.c.Win32_Process.watch_for("creation")

        print("Observando novos processos...")

        # Início do HONEYPOT
        # diretorios = honeypot.iniciar()

        # observer = Observer()
        # observer.start()

        # for diretorio in diretorios:
        #     observer.schedule(self.evento_handler, diretorio + r"\acertificados", recursive=True)
        #     observer.schedule(self.evento_handler, diretorio + r"\zcurriculos", recursive=True)

        try:
            
            while self.monitoramento_ativo:

                try:

                    new_process = self.process_watcher()
                    
                    if (self.evento_handler.pasta_modificada):
                        os.kill(new_process.ProcessId, signal.SIGILL)
                        break

                    self.analise_instancia(new_process.ProcessId, new_process)

                except ValueError:
                    pass

            if self.monitoramento_ativo == False:
                self.process_watcher.stop()
                self.process_watcher.cancel()
                observer.stop()

        except KeyboardInterrupt:
            self.process_watcher.stop()
            self.process_watcher.cancel()
            pass


    def analise_instancia(self, pid, processo):

        processo_registrado = colecao_processos.find_one({"nomeProcesso": processo.Name, "uuid": self.id})

        if (processo_registrado):
            
            print('--------- PROCESSO MAPEADO ---------')
            print(f"Análise do processo: '{processo.Name}':")

            if (processo_registrado['status'] == 'ameaça'):
                os.kill(pid, signal.SIGILL)

            if (processo_registrado['status'] == 'suspeito'):
                print('PROCESSO SUSPEITO', processo_registrado['nomeProcesso'])
            
        else: 

            print('--------- NOVO PROCESSO ENCONTRADO ---------')
            print(f"Análise do processo: '{processo.Name}':")
            # Estrutura de análise
            # dados_analise = {
            #     "handleCount": 0,
            #     "pageFaults": 0,
            #     "pageFileUsage": 0,
            #     "peakPageFileUsage": 0,
            #     "workingSetSize": 0,
            #     "threadCount": 0,
            #     "priority": 0,
            #     "privatePageCount": 0
            # }

            # dados_analise["handleCount"] = int(int(processo.handleCount) > MAX_HANDLE_COUNT)
            # dados_analise["pageFaults"] = int(int(processo.pageFaults) > MAX_PAGE_FAULTS)
            # dados_analise["pageFileUsage"] = int(int(processo.pageFileUsage) > MAX_PAGE_FILE_USAGE)
            # dados_analise["peakPageFileUsage"] = int(int(processo.peakPageFileUsage) > MAX_PEAK_PAGE_FILE_USAGE)
            # dados_analise["workingSetSize"] = int(int(processo.workingSetSize) > MAX_WORKING_SET_SIZE)
            # dados_analise["threadCount"] = int(int(processo.threadCount) > MAX_THREAD_COUNT)
            # dados_analise["priority"] = int(int(processo.priority) > MAX_PRIORITY)
            # dados_analise["privatePageCount"] = int(int(processo.privatePageCount) > MAX_PRIVATE_PAGE_COUNT)
            try:
                processo_analise = psutil.Process(pid) 
                
                dados_analise = {
                    "handleCount": int(int(processo_analise.num_handles()) > MAX_HANDLE_COUNT),
                    "pageFaults": int(int(processo_analise.memory_info().num_page_faults) > MAX_PAGE_FAULTS),
                    "pageFileUsage": int(int(processo_analise.memory_info().pagefile) > MAX_PAGE_FILE_USAGE),
                    "peakPageFileUsage": int(int(processo_analise.memory_info().peak_pagefile) > MAX_PEAK_PAGE_FILE_USAGE),
                    "workingSetSize": int(int(processo_analise.memory_info().rss) > MAX_WORKING_SET_SIZE),
                    "threadCount": int(int(processo_analise.num_threads()) > MAX_THREAD_COUNT),
                    "priority": int(int(processo.Priority) > MAX_PRIORITY),
                    "privatePageCount": int(int(processo_analise.memory_info().private) > MAX_PRIVATE_PAGE_COUNT)
                }

                dados_processo = {
                    "handleCount": processo_analise.num_handles(),
                    "pageFaults": processo_analise.memory_info().num_page_faults,
                    "pageFileUsage": processo_analise.memory_info().pagefile,
                    "peakPageFileUsage": processo_analise.memory_info().peak_pagefile,
                    "workingSetSize": processo_analise.memory_info().rss,
                    "threadCount": processo_analise.num_threads(),
                    "priority": processo.Priority,
                    "privatePageCount": processo_analise.memory_info().private
                }

                # resposta_ml = self.classif.predict([[
                #     processo_analise.num_handles(),
                #     processo_analise.memory_info().num_page_faults,
                #     processo_analise.memory_info().pagefile,
                #     processo_analise.memory_info().peak_pagefile,
                #     processo_analise.memory_info().rss,
                #     processo_analise.num_threads(),
                #     processo_analise.memory_info().private
                # ]])
                resposta_ml = 0

                if (resposta_ml == 1):
                    os.kill(pid, signal.SIGILL)
                    status = 'ameaça'
                    print(f"O Processo {processo.Name} é uma AMEAÇA.")
                else:
                    # Validação inicial caso o processo seja muito malígno
                    status = self.validarResultados(pid, dados_analise)

                if (status == 'ameaça'):
                    print(f"O Processo {processo.Name} é uma AMEAÇA.")

                else:

                    # Loop de avaliação por dois segundos
                    tempo_inicio = time.time()
                    dados_analise = []
                    dados_processo_durante = []

                    while time.time() - tempo_inicio < 2:
                            
                        processo_analise = psutil.Process(pid)

                        # Análise
                        obj_boolean = {}
                        obj_processo = {}

                        obj_boolean["handleCount"] = int(int(processo_analise.num_handles()) > MAX_HANDLE_COUNT)
                        obj_boolean["pageFaults"] = int(int(processo_analise.memory_info().num_page_faults) > MAX_PAGE_FAULTS)
                        obj_boolean["pageFileUsage"] = int(int(processo_analise.memory_info().pagefile) > MAX_PAGE_FILE_USAGE)
                        obj_boolean["peakPageFileUsage"] = int(int(processo_analise.memory_info().peak_pagefile) > MAX_PEAK_PAGE_FILE_USAGE)
                        obj_boolean["workingSetSize"] = int(int(processo_analise.memory_info().rss) > MAX_WORKING_SET_SIZE)
                        obj_boolean["threadCount"] = int(int(processo_analise.num_threads()) > MAX_THREAD_COUNT)
                        obj_boolean["priority"] = int(int(processo.Priority) > MAX_PRIORITY)
                        obj_boolean["privatePageCount"] = int(int(processo_analise.memory_info().private) > MAX_PRIVATE_PAGE_COUNT)

                        obj_processo["handleCount"] = processo_analise.num_handles()
                        obj_processo["pageFaults"] = processo_analise.memory_info().num_page_faults
                        obj_processo["pageFileUsage"] = processo_analise.memory_info().pagefile
                        obj_processo["peakPageFileUsage"] = processo_analise.memory_info().peak_pagefile
                        obj_processo["workingSetSize"] = processo_analise.memory_info().rss
                        obj_processo["threadCount"] = processo_analise.num_threads()
                        obj_processo["priority"] = processo.Priority
                        obj_processo["privatePageCount"] = processo_analise.memory_info().private

                        dados_analise.append(obj_boolean)
                        dados_processo_durante.append(obj_processo)

                        status = self.validarResultados(pid, obj_boolean)

                        if (status == 'ameaça'):
                            break

                        time.sleep(0.5)

                colecao_analise.insert_one({
                    'nomeProcesso': processo.Name,
                    'pid': pid,
                    'dadosAnalise': dados_analise,
                    'dadosProcessoDurante': dados_processo_durante,
                    'dadosProcesso': dados_processo,
                    'status': status,
                    'uuid': self.id
                })

                # Salvar para análise no banco
                colecao_processos.insert_one({
                    'nomeProcesso': processo.Name,
                    'pid': pid,
                    'dadosAnalise': dados_analise,
                    'dadosProcesso': dados_processo,
                    'status': status,
                    'uuid': self.id
                })

                print(f"O processo: '{processo.Name}' é {status}")

            except psutil.NoSuchProcess:
                print("Processo não encontrado. Continuando a execução do programa.")

            except PermissionError:
                print(f"Erro de permissão. Continuando a execução do programa.")


    def validarResultados(self, pid, resultados):

        retorno = ''

        if (sum(resultados.values()) > 4) or (self.evento_handler.pasta_modificada and sum(resultados.values()) > 2):

            retorno = 'ameaça'

            os.kill(pid, signal.SIGILL)

            print(f"AMEAÇA NEUTRALIZADA.")

        elif sum(resultados.values()) > 2:

            retorno = 'suspeito'
            print(f"Processo SUSPEITO devido a valores ultrapassados. SOB ANÁLISE")

        else:
            retorno = 'seguro'

        return retorno


    def machine_learning_iniciar(self):

        caminho_arquivo = os.path.join(os.path.dirname(__file__), '..', 'config', 'machine_learning.json')

        # Verificar se o arquivo existe, caso contrário, criá-lo
        if not os.path.exists(caminho_arquivo):

            features = []
            labels = []

            for processo in list(colecao_analise.find()):
                
                for dado_analise_durante in processo['dadosProcessoDurante']:

                    molde_processo = (
                        dado_analise_durante['handleCount'],
                        dado_analise_durante['pageFaults'],
                        dado_analise_durante['pageFileUsage'],
                        dado_analise_durante['peakPageFileUsage'],
                        dado_analise_durante['workingSetSize'],
                        dado_analise_durante['threadCount'],
                        dado_analise_durante['privatePageCount'],
                    )

                    features.append(molde_processo)

                    if processo['status'] == "seguro":
                        labels.append(0)
                    elif (processo['status'] == "suspeito" or processo['status'] == "ameaça"):
                        labels.append(1)
                    else:
                        labels.append(1)

            dados_principais = {
                "features": features,
                "labels": labels
            }

            with open(caminho_arquivo, "w") as arquivo:
                json.dump(dados_principais, arquivo, indent=4)

        else:

            with open(caminho_arquivo, "rb") as arquivo:
                dados_existentes = json.load(arquivo)

                features = dados_existentes['features']
                labels = dados_existentes['labels']

        print(features)
        self.classif.fit(features, labels)
    

    def pegar_uuid(self):

        mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(2, -1, -1)])
        return str(uuid.uuid5(uuid.NAMESPACE_DNS, mac))
    

    def status_health(self):
        return self.monitoramento_ativo

monitoramento = Monitoramento()
