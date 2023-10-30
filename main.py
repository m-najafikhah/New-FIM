import sys
import os
sys.path.append(r"C:\users\mohammad\appdata\local\programs\python\python311\lib\site-packages")

import time
import watchdog.events as events
import watchdog.observers as observers

class FolderMonitor(object):
    def __init__(self, folder_path):
        self.observer = observers.Observer()
        self.event_handler = events.FileSystemEventHandler()
        self.event_handler.on_created = self.on_created
        self.event_handler.on_deleted = self.on_deleted
        self.event_handler.on_modified = self.on_modified
        self.observer.schedule(self.event_handler, folder_path, recursive=True)

    def start(self):
        self.observer.start()

    def stop(self):
        self.observer.stop()
        self.observer.join()

    def on_created(self, event):
        print(f"File/folder created: {event.src_path}")

    def on_deleted(self, event):
        print(f"File/folder deleted: {event.src_path}")

    def on_modified(self, event):
        file_path = event.src_path
        file_name = os.path.basename(file_path)
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")

        with open(r"folder_monitor.log", r"a") as f:
            f.write(f"{current_time}: File {file_name} | {event.src_path} was modified.\n")


if __name__ == "__main__":
    folder_path = (r'C:\Users\Mohammad\Desktop\TestHash')
    monitor = FolderMonitor(folder_path)
    monitor.start()

    # Keep the program running until the user presses Enter
    input("Press Enter to stop monitoring...")
    monitor.stop()
