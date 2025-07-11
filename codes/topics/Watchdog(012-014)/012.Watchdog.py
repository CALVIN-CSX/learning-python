import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Set the path to the folder you want to monitor
folder_to_watch = "mylocalpath/learning-python/codes/topics/Watchdog(012-/Watchme"  # Replace with your actual path

# Define a custom handler by subclassing FileSystemEventHandler
class Watchdog(FileSystemEventHandler):
    # Triggered when a file or folder is created in the watched directory
    def on_created(self, event):
        if not event.is_directory:
            file_name = os.path.basename(event.src_path)
            print(f"✅ File created at: {event.src_path}")
            print(f"📄 File name: {file_name}")

# Create an instance of your handler
event_handler = Watchdog()

# Set up the observer and schedule it to monitor the folder
observer = Observer()
observer.schedule(event_handler, folder_to_watch, recursive=False)  # Set recursive=True to monitor subdirectories

# Start watching
observer.start()
print(f"🔍 Now watching: {folder_to_watch}")

# Keep the script running to listen for events
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("🛑 Stopping observer...")
    observer.stop()

# Wait until the thread terminates
observer.join()

"""
output:
 File created at: mylocalpath/learning-python/codes/topics/Watchdog(012-/Watchme\New Text Document.txt
 File name: New Text Document.txt
 File created at: mylocalpath/learning-python/codes/topics/Watchdog(012-/Watchme\New Text Document.txt
 File name: New Text Document.txt
"""
#used chatgtp to make the code more clean to look at for future references