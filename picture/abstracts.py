import abc
import datetime
from typing import Tuple

from PIL import Image, ImageFilter, ImageDraw, ImageFont, UnidentifiedImageError


class Picture(abc.ABC):

    @abc.abstractmethod
    def resize(self, sizes: Tuple[int]):
        pass

    @abc.abstractmethod
    def apply_filter(self, filter_name: str = None):
        pass

    @abc.abstractmethod
    def put_the_date(self):
        pass

    @abc.abstractmethod
    def open(self, path: str):
        pass

    @abc.abstractmethod
    def save(self, path: str):
        pass


class JPGPicture(Picture):

    def __init__(self):
        self.picture = None
        self.filename = ''
        self.file_extension = 'jpeg'

    def resize(self, sizes: Tuple[int]):
        self.picture = self.picture.resize(sizes)
        return self.picture

    def apply_filter(self, filter_name: str = None):
        self.picture = self.picture.filter(ImageFilter.SMOOTH)
        return self.picture

    def put_the_date(self):
        font = ImageFont.load_default()
        pencil = ImageDraw.Draw(self.picture)
        pencil.text(
            (300, 350),
            f'{datetime.date.today()}',
            font=font,
            fill='red',
            size=42,
        )
        return self.picture

    def open(self, path: str):
        self.picture = Image.open(path)
        self.filename = path.split("/")[-1].split(".")[0]
        return self.picture

    def save(self, path: str):
        filename = f'{self.filename}_{datetime.datetime.now()}'
        self.picture.save(path + f'{filename}.{self.file_extension}')


class BMPPicture(Picture):

    def __init__(self):
        self.picture = None
        self.filename = ''
        self.file_extension = 'bmp'

    def resize(self, sizes: tuple):
        self.picture = self.picture.resize((400, 400))
        return self.picture

    def apply_filter(self, filter_name: str = None):
        self.picture = self.picture.filter(ImageFilter.SMOOTH)
        return self.picture

    def put_the_date(self):
        font = ImageFont.load_default()
        pencil = ImageDraw.Draw(self.picture)
        pencil.text(
            (300, 350),
            f'{datetime.date.today()}',
            font=font,
            fill='red',
            size=42,
        )
        return self.picture

    def open(self, path: str):
        self.picture = Image.open(path)
        self.filename = path.split("/")[-1].split(".")[0]
        return self.picture

    def save(self, path: str):
        filename = f'{self.filename}_{datetime.datetime.now()}'
        self.picture.save(path + f'{filename}.{self.file_extension}')
