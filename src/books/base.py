from abc import ABC, abstractmethod

from src.exceptions import BookValidationError

class BaseBook(ABC):
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str):
        self._validate(year, isbn)
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn

    def _validate(self, year: int, isbn: str):
        if year < 0:
            raise BookValidationError(f'Год издания не может быть отрицательным: {year}')
        if len(isbn) < 3:
            raise BookValidationError(f'Слишком короткий ISBN: {isbn}')

    @abstractmethod
    def get_format(self) -> str:
        ...

    def __repr__(self) -> str:
        return f'{self.get_format()} "{self.title}" ({self.author}, {self.year}, {self.isbn})'

    def __eq__(self, other):
        if not isinstance(other, BaseBook):
            return NotImplemented
        return self.isbn == other.isbn

    def __hash__(self):
        return hash(self.isbn)
