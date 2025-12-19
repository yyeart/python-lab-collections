from src.books.base import BaseBook
from src.collections.base import BaseIndex

class ISBNIndex(BaseIndex):
    def add(self, book: BaseBook) -> None:
        self._data[book.isbn] = book

    def remove(self, book: BaseBook) -> None:
        if book.isbn in self._data:
            del self._data[book.isbn]
