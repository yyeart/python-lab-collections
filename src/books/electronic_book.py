from src.books.base import BaseBook
from src.exceptions import BookValidationError

class EBook(BaseBook):
    """
    Класс ,представляющий электронную книгу
    """
    def __init__(self, title: str, author: str, year: int,
                 genre: str, isbn: str, file_size: float,
                 file_format: str):
        super().__init__(title, author, year, genre, isbn)
        if file_size <= 0:
            raise BookValidationError(f'Размер файла должен быть положительным: {file_size}')
        self.file_size=  file_size
        self.file_format = file_format

    def get_format(self) -> str:
        return 'Электронная книга'
