import time, os

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

class monitora_arquivos(FileSystemEventHandler):
    def on_created(self, event):
        nome_arquivo = os.path.basename(event.src_path)
        print(f'Arquivo adicionado: {nome_arquivo}')

observador = Observer()
monitor = monitora_arquivos()

observador.schedule(monitor, r'C:\Users\jotap\OneDrive\Área de Trabalho\Arquivos', recursive=False)
        
observador.start()

while True:
    time.sleep(1)