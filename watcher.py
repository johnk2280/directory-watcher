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
PICTURE_MAPPER = {
    'jpg': JPGPicture,
    'bmp': BMPPicture,
}


class Handler(FileSystemEventHandler):

    def on_created(self, event):
        file_extension = event.src_path.split('.')[-1]
        try:
            picture = PICTURE_MAPPER[file_extension]().open(event.src_path)
            picture.resize((400, 400))
            picture.apply_filter()
            picture.put_the_date()
            picture.save(PATH_TO)

        # Открытие изображения
        # img = Image.open(event.src_path)

        # Изменение размеров изображения
        # new_img = img.resize((400, 400))

        # Наложение размытия
        # new_img = new_img.filter(ImageFilter.SMOOTH)

        # Наложение текущей даты
        # font = ImageFont.load_default()
        # pencil = ImageDraw.Draw(new_img)
        # pencil.text(
        #     (300, 350),
        #     f'{datetime.date.today()}',
        #     font=font,
        #     fill='red',
        #     size=42,
        # )

        # Добавление соли к имени файла для избежания коллизий.
        # filename = f'{event.src_path.split("/")[-1].split(".")[0]}' \
        #            f'_{datetime.datetime.now()}'
        # new_img.save(
        #     PATH_TO.joinpath(f'{filename}.{file_extension}').as_posix(),
        # )
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
