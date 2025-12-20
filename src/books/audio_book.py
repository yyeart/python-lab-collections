from src.books.base import BaseBook
from src.exceptions import BookValidationError

class AudioBook(BaseBook):
    """
    Класс ,представляющий аудио книгу
    """
    def __init__(self, title: str, author: str, year: int,
                 genre: str, isbn: str, duration: int,
                  bitrate: int, narrator: str):
        super().__init__(title, author, year, genre, isbn)
        if duration <= 0:
            raise BookValidationError(f'Длительность должна быть положительной: {duration}')
        self.duration = duration
        self.bitrate = bitrate
        self.narrator = narrator

    def get_format(self) -> str:
        return 'Аудио книга'
