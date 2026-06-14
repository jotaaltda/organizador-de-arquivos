import time, os

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from colorama import Fore, init

init(autoreset=True)

class monitora_arquivos(FileSystemEventHandler):
    def on_created(self, event):
        nome_arquivo = os.path.basename(event.src_path)
        tipo_arquivo = os.path.splitext(nome_arquivo)
        print(f'Arquivo adicionado: {Fore.YELLOW + nome_arquivo}, extensão: {Fore.YELLOW + tipo_arquivo[1]}')

observador = Observer()
monitor = monitora_arquivos()

observador.schedule(monitor, r'C:\Users\jotap\OneDrive\Área de Trabalho\Arquivos', recursive=False)
        
observador.start()

while True:
    time.sleep(1)