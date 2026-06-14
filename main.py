from watchdog.events import FileSystemEventHandler

class monitora_arquivos(FileSystemEventHandler):
    def on_created(self, event):
        print(event.src_path)
        