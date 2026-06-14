import time, os

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from colorama import Fore, Style, init

init(autoreset=True)

class monitora_arquivos(FileSystemEventHandler):
    def on_created(self, event):
        nome_arquivo = os.path.basename(event.src_path)
        nome, extensao = os.path.splitext(nome_arquivo)
        categoria = tipo_arquivo[extensao]
        print(f'Arquivo adicionado: {Fore.YELLOW + nome_arquivo + Style.RESET_ALL}. Extensão: {Fore.YELLOW + extensao + Style.RESET_ALL}, categoria: {Fore.YELLOW + categoria + Style.RESET_ALL}')

observador = Observer()
monitor = monitora_arquivos()

observador.schedule(monitor, r'C:\Users\jotap\OneDrive\Área de Trabalho\Arquivos', recursive=False)
        
observador.start()

tipo_arquivo = {
    '.txt': 'Documentos',
    '.pdf': 'Documentos',

    '.png': 'Imagens',
    '.jpg': 'Imagens',

    '.mp3': 'Músicas e Sons',
    '.mp4': 'Vídeos',

    '.zip': 'ZIPs'
}

while True:
    time.sleep(1)