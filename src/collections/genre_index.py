from src.books.base import BaseBook
from src.collections.base import BaseIndex
from src.exceptions import BookNotFoundError


class GenreIndex(BaseIndex):
    def add(self, book: BaseBook) -> None:
        if book.genre not in self._data:
            self._data[book.genre] = []
        self._data[book.genre].append(book)

    def remove(self, book: BaseBook) -> None:
        if book.genre not in self._data:
            raise BookNotFoundError
        items = self._data[book.genre]
        if book in items:
            items.remove(book)
            if not items:
                del self._data[book.genre]
