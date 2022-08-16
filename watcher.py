import time
from pathlib import Path

from PIL import UnidentifiedImageError

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from picture.abstracts import BMPPicture
from picture.abstracts import JPGPicture

PATH = Path(__file__).resolve().parent
PATH_FROM = PATH.joinpath('./temp/')
PATH_TO = PATH.joinpath('./processed/')

# Выполнено на примере 2-х форматов.
FORMAT_MAPPER = {
    'jpg': JPGPicture,
    'bmp': BMPPicture,
}


class Handler(FileSystemEventHandler):

    def on_created(self, event):
        file_extension = event.src_path.split('.')[-1]
        try:
            picture = FORMAT_MAPPER[file_extension]().open(event.src_path)
            picture.resize((400, 400))
            picture.apply_filter()
            picture.put_the_date()
            picture.save(PATH_TO)
        except (KeyError, UnidentifiedImageError):
            pass

        print('on_created', event.event_type, event.src_path)


if __name__ == '__main__':
    handler = Handler()
    observer = Observer()
    observer.schedule(handler, path=PATH_FROM.as_posix(), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
