import psutil  
import os, signal
import wmi
import sys
import time
from sklearn import tree 

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'database'))
from conexao_db  import instanciar_processos, instanciar_analise

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

class Monitoramento:

    def __init__(self):
        self.monitoramento_ativo = False


    def parar(self):
        self.monitoramento_ativo = False

 
    def iniciar(self):

        ia = importaIA()

        c = wmi.WMI(privileges=["Security"])
        process_watcher = c.Win32_Process.watch_for("creation")
        self.monitoramento_ativo = True

        print("Observando novos processos... Pressione Ctrl+C para sair.")

        try:
            while self.monitoramento_ativo:
                new_process = process_watcher()
                print(new_process)
                processo_ia = psutil.Process(new_process.ProcessId) 
                media = ia.predict([processo_ia.num_handles(),
                     processo_ia.memory_info().num_page_faults,
                     processo_ia.memory_info().pagefile,
                     processo_ia.memory_info().peak_pagefile,
                     processo_ia.memory_info().rss,
                     processo_ia.num_threads(),
                     new_process.Priority,
                     processo_ia.memory_info().private])
                
                    #decisao se é seguro ou ameaca
                if media == 1:

                    os.kill(new_process.ProcessId, signal.SIGILL)

                    print(f"AMEAÇA NEUTRALIZADA.")
                    continue
                    

                self.analise_instancia(new_process.ProcessId, new_process)
        except KeyboardInterrupt:
            pass



    def analise_instancia(self, pid, processo):

        processo_registrado = colecao_processos.find_one({"nomeProcesso": processo.Name})

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
                    'status': status
                })

                # Salvar para análise no banco
                colecao_processos.insert_one({
                    'nomeProcesso': processo.Name,
                    'pid': pid,
                    'dadosAnalise': dados_analise,
                    'dadosProcesso': dados_processo,
                    'status': status
                })

            except psutil.NoSuchProcess:
                print("Processo não encontrado. Continuando a execução do programa.")

            except PermissionError:
                print(f"Erro de permissão. Continuando a execução do programa.")


    def validarResultados(self, pid, resultados):

        retorno = ''

        if sum(resultados.values()) > 4:

            retorno = 'ameaça'

            os.kill(pid, signal.SIGILL)

            print(f"AMEAÇA NEUTRALIZADA.")

        elif sum(resultados.values()) > 2:

            retorno = 'suspeito'
            print(f"Processo SUSPEITO devido a valores ultrapassados. SOB ANÁLISE")


        else:
            retorno = 'seguro'

        return retorno


def validarResultados(pid, resultados):

    retorno = ''

    if sum(resultados.values()) > 4:

        retorno = 'ameaça'

        os.kill(pid, signal.SIGILL)

        print(f"AMEAÇA NEUTRALIZADA.")

    elif sum(resultados.values()) > 2:

        retorno = 'suspeito'
        print(f"Processo SUSPEITO devido a valores ultrapassados. SOB ANÁLISE")


    else:
        retorno = 'seguro'

    return retorno


#iniciar()

# CÓDIGO ABAIXO É PARA AVALIAR RESULTADOS DO MONGODB


def importaIA():

    colecao_processos.find()
    documentos = list(colecao_processos.find())

    arrayStatus = []
    array = []

    for doc in documentos:
        features = []
        features.append(doc["dadosProcesso"]["handleCount"])
        features.append(doc["dadosProcesso"]["pageFaults"])
        features.append(doc["dadosProcesso"]["pageFileUsage"])
        features.append(doc["dadosProcesso"]["peakPageFileUsage"])
        features.append(doc["dadosProcesso"]["workingSetSize"])
        features.append(doc["dadosProcesso"]["threadCount"])
        features.append(doc["dadosProcesso"]["priority"])
        features.append(doc["dadosProcesso"]["privatePageCount"])
        array.append(features)
        if doc["status"] == "seguro":
            arrayStatus.append(0)
        else:
            arrayStatus.append(1)    

    classif = tree.DecisionTreeClassifier() #Classificador
    
    classif.fit (array, arrayStatus)
    
    return classif

    