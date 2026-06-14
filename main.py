import time, os, shutil

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from colorama import Fore, Style, init

init(autoreset=True)

class monitora_arquivos(FileSystemEventHandler):
    def on_created(self, event):
        nome_arquivo = os.path.basename(event.src_path)
        nome, extensao = os.path.splitext(nome_arquivo)

        try:
            categoria = tipo_arquivo[extensao]
        except KeyError:
            categoria = 'Outros'

        print(f'Arquivo adicionado: {Fore.YELLOW + nome_arquivo + Style.RESET_ALL}, extensão: {Fore.YELLOW + extensao + Style.RESET_ALL}')

        destino = os.path.join(r'C:\Users\jotap\OneDrive\Área de Trabalho\Arquivos', categoria, nome_arquivo)

        shutil.move(event.src_path, destino, copy_function=shutil.copy2)

observador = Observer()
monitor = monitora_arquivos()

observador.schedule(monitor, r'C:\Users\jotap\OneDrive\Área de Trabalho\Arquivos', recursive=False)

tipo_arquivo = {
    '.txt': 'Documentos',
    '.pdf': 'Documentos',

    '.png': 'Imagens',
    '.jpg': 'Imagens',

    '.mp3': 'Músicas e Sons',
    '.mp4': 'Vídeos',

    '.zip': 'ZIPs',

    '.exe': 'Programas'
}

observador.start()

while True:
    time.sleep(1)