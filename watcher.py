import logging
import sys
import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from watcher import runner
def onCreate(event):
runner()
if __name__ == "__main__":
logging.basicConfig(level=logging.INFO,
format='%(asctime)s - %(message)s',
datefmt='%Y-%m-%d %H:%M:%S')
path = sys.argv[1] if len(sys.argv) > 1 else '.'
event_handler = FileSystemEventHandler()
# calling functions
event_handler.on_created = onCreate
path1 = "/content/drive/MyDrive/Attendance"
observer = Observer()
observer.schedule(event_handler, path1, recursive=True)
observer.start()
try:
print("Monitoring Drive Folder")
while True:
time.sleep(30)
except KeyboardInterrupt:
observer.stop()
observer.join()
