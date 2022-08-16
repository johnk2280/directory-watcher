import abc
import datetime
from pathlib import Path
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
    def save(self, path: Path):
        pass


class JPGPicture(Picture):

    def __init__(self):
        self.picture = None
        self.filename = ''
        self.file_extension = 'jpeg'

    def resize(self, sizes: Tuple[int]):
        self.picture = self.picture.resize(sizes)
        return self

    def apply_filter(self, filter_name: str = None):
        self.picture = self.picture.filter(ImageFilter.SMOOTH)
        return self

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
        return self

    def open(self, path: str):
        self.picture = Image.open(path)
        self.filename = path.split("/")[-1].split(".")[0]
        return self

    def save(self, path: Path):
        filename = f'{self.filename}_{datetime.datetime.now()}'
        self.picture.save(path.joinpath(f'{filename}.{self.file_extension}'))


class BMPPicture(Picture):

    def __init__(self):
        self.picture = None
        self.filename = ''
        self.file_extension = 'bmp'

    def resize(self, sizes: Tuple[int]):
        self.picture = self.picture.resize(sizes)
        return self

    def apply_filter(self, filter_name: str = None):
        self.picture = self.picture.filter(ImageFilter.SMOOTH)
        return self

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
        return self

    def open(self, path: str):
        self.picture = Image.open(path)
        self.filename = path.split("/")[-1].split(".")[0]
        return self

    def save(self, path: Path):
        filename = f'{self.filename}_{datetime.datetime.now()}'
        self.picture.save(path.joinpath(f'{filename}.{self.file_extension}'))
