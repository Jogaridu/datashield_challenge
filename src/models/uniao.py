import time
import logging
import os
import psutil  # Importe a biblioteca psutil
from signal import SIGILL
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler
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
        return caminho


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

class MyEventHandler(FileSystemEventHandler):
    def __init__(self):
        self.folder_modified = False
    
    def on_any_event(self, event):
        self.folder_modified = True


def folder_monitor(caminho_pasta):

    print("Observador iniciado HONEYPOT")

    # event_handler = LoggingEventHandler()
    event_handler = MyEventHandler()
    observer = Observer()

    logging.basicConfig(
        level=logging.INFO, format='%(asctime)s - PID:%(process)d - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    observer.schedule(event_handler, caminho_pasta, recursive=True)
    observer.start()

    while True:
        observer.join()
    return {'instancia': observer, 'evento': event_handler.folder_modified}
    # try:
        
    # except KeyboardInterrupt:
    #     observer.stop()
    #     observer.join()


# caminho_pasta = gitclone()
# print(caminho_pasta)
# pasta_oculta(caminho_pasta)
# folder_monitor(caminho_pasta)