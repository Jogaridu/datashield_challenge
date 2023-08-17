import time
import logging
import os
import psutil  # Importe a biblioteca psutil
from signal import SIGTERM
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

pid = os.getpid()
print(pid)

event_handler = LoggingEventHandler()
observer = Observer()

folder = r"D:\1TDCG\challenge\vitima"

def folder_monitor(folder):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    observer.schedule(event_handler, folder, recursive=True)
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

folder_monitor(folder)
