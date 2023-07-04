import time
import logging
import multiprocessing
import os
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
print(os.getpid())

#Inicialização
event_handler = LoggingEventHandler()
observer = Observer()

folder = "G:\Meus Documentos\Área de Trabalho\documentos"
folder1 = "C:\Área de Trabalho"

def folder_monitor(folder):
    print(123)
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    observer.schedule(event_handler, folder, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()



folder_monitor(folder)


