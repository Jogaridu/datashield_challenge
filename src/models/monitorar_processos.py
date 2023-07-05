import psutil

def verifica_processo_alterando_arquivos(processo_pid):
    processo = psutil.Process(processo_pid)
    print(processo)
    arquivos_abertos = processo.open_files()
    print(arquivos_abertos)
    return len(arquivos_abertos) > 100


def iniciar():
    # Dicionário para rastrear os processos atuais
    processos_atuais = {}

    while True:
        # Obtém a lista de processos em execução
        processos = psutil.process_iter()

        try:

            # Verifica novos processos e processos encerrados
            for processo in processos:
                pid = processo.pid

                if pid not in processos_atuais:
                    processos_atuais[pid] = processo
                    if verifica_processo_alterando_arquivos(pid):
                        print(f"Novo processo detectado: PID {pid} está alterando múltiplos arquivos.")

            # Remove processos encerrados da lista de processos atuais
            for pid in list(processos_atuais):
                if not psutil.pid_exists(pid):
                    del processos_atuais[pid]

        except ValueError:
            print(ValueError)

        # Aguarda por eventos de novos processos
        psutil.wait_procs(processos, timeout=1)
