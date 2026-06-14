from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

class monitora_arquivos(FileSystemEventHandler):
    def on_created(self, event):
        print(event.src_path)

observador = Observer()
monitor = monitora_arquivos()

observador.schedule(monitor, r'C:\Users\jotap\OneDrive\Área de Trabalho\Arquivos', recursive=False)
        
