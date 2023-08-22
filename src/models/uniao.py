import time
import logging
import os
import psutil  # Importe a biblioteca psutil
from signal import SIGTERM
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import subprocess
import git
import win32file
import win32con


def gitclone():

    resultado = subprocess.check_output('whoami', shell=True)
    saidacmd = resultado.decode('utf-8').strip()

    saidadiv = saidacmd.split("\\")
    nomeuser = saidadiv[-1]

    caminho = f"C:\\Users\\{nomeuser}\\Desktop\\1honeypot"

    url_repo = "https://github.com/pedr0aug/honey.git"
    
    try:
         
        git.Repo.clone_from(url_repo, caminho)

        print(f"Repositório clonado em: {caminho}")

        return caminho 
    except:
        print(f"Repositório {caminho} ja existe ")


def pasta_oculta(caminho_pasta):

    try:
        # Obtém os atributos atuais da pasta
        atributos_atuais = win32file.GetFileAttributesW(caminho_pasta)

        # Define o atributo de oculto
        novo_atributo = atributos_atuais | win32con.FILE_ATTRIBUTE_HIDDEN

        # Atualiza os atributos da pasta
        win32file.SetFileAttributesW(caminho_pasta, novo_atributo)
        print(f"Pasta '{caminho_pasta}' foi tornada oculta com sucesso!")
    except Exception as e:
        print(f"Erro ao tornar a pasta oculta: {e}")


def folder_monitor(caminho_pasta):
        
    pid = os.getpid()
    print("Observador iniciado | PID:",pid)

    event_handler = LoggingEventHandler()
    observer = Observer()

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - PID:%(process)d - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    observer.schedule(event_handler, caminho_pasta, recursive=True)
    observer.start()

    try:
            while True:
                time.sleep(1)
                # Obtendo a lista de processos em execução
                for proc in psutil.process_iter(['pid', 'name']):
                    try:
                        process_id = proc.info['pid']
                        process_name = proc.info['name']
                        if process_name == 'kidransomware.exe':
                            print(f"Processo de ransomware detectado! ID: {process_id}")
                            os.kill(process_id, SIGTERM)
                            print("processo finalizado!")
                    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                        pass
    except KeyboardInterrupt:
            observer.stop()
            observer.join()    


caminho_pasta = gitclone()
pasta_oculta(caminho_pasta)
folder_monitor(caminho_pasta)

