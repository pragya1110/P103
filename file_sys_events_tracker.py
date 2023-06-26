import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

frm_dir="C:/Users/pragy/OneDrive/Desktop/projects/project102"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        name,ext=os.path.splitext(event.src_path)
        time.sleep(3)
        fn=os.path.basename(event.src_path)
        print(fn+" has been created")
    def on_deleted(self, event):
        print(os.path.basename(event.src_path)+" has been deleted")
    def on_moved(self, event):
        print(os.path.basename(event.src_path)+" has been moved or renamed")
    def on_modified(self, event):
        print(os.path.basename(event.src_path)+" has been modified")

event_handler = FileEventHandler()

observer = Observer()

observer.schedule(event_handler, frm_dir, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("Do not interrupt me!")
    observer.stop()
    