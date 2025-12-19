from src.books.base import BaseBook
from src.exceptions import BookValidationError

class PrintedBook(BaseBook):
    def __init__(self, title: str, author: str, year: int,
                 genre: str, isbn: str, pages_count: int, weight: int):
        super().__init__(title, author, year, genre, isbn)
        if pages_count <= 0:
            raise BookValidationError(f'Количество страниц должно быть положительным: {pages_count}')
        self.pages_count = pages_count
        self.weight = weight

    def get_format(self) -> str:
        return 'Печатная книга'
