from src.books.base import BaseBook
from src.collections.base import BaseIndex

class ISBNIndex(BaseIndex):
    """
    Индекс для поиска книг по уникальному номеру ISBN
    """
    def add(self, book: BaseBook) -> None:
        self._data[book.isbn] = book

    def remove(self, book: BaseBook) -> None:
        if book.isbn in self._data:
            del self._data[book.isbn]
