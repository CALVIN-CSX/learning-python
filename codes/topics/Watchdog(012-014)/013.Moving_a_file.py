import os
import shutil
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source_folder = "localfiles\learning-python\codes\topics\Watchdog(012-"
dest = "localfiles\\learning-python\\codes\\topics\\Watchdog(012-\\Watchme"

class Move(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            filename = os.path.basename(event.src_path)
            filesrc = event.src_path
            dest_path = os.path.join(dest, filename)
            shutil.move(filesrc, dest_path)
            print(f"Moved {filesrc} to {dest_path}")

eventhandler = Move()
observer = Observer()
observer.schedule(eventhandler, source_folder, recursive=False)
observer.start()
print(f"Watchdog started on {source_folder}")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()

"""
Output
Watchdog started on localfiles\learning-python\codes\topics\Watchdog(012-
Moved localfiles\learning-python\codes\topics\Watchdog(012-\move_me_to_Watchme_using_watchdog.txt to
 localfiles\learning-python\codes\topics\Watchdog(012-\Watchme\move_me_to_Watchme_using_watchdog.txt

"""
