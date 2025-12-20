from src.books.base import BaseBook
from src.collections.base import BaseIndex
from src.exceptions import BookNotFoundError


class YearIndex(BaseIndex):
    """
    Индекс для группировки и поиска книг по году издания
    """
    def add(self, book: BaseBook) -> None:
        if book.year not in self._data:
            self._data[book.year] = []
        self._data[book.year].append(book)

    def remove(self, book: BaseBook) -> None:
        if book.year not in self._data:
            raise BookNotFoundError
        items = self._data[book.year]
        if book in items:
            items.remove(book)
            if not items:
                del self._data[book.year]
