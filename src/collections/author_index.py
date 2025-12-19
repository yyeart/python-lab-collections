from src.books.base import BaseBook
from src.collections.base import BaseIndex
from src.exceptions import BookNotFoundError

class AuthorIndex(BaseIndex):
    def add(self, book: BaseBook) -> None:
        if book.author not in self._data:
            self._data[book.author] = []
        self._data[book.author].append(book)

    def remove(self, book: BaseBook) -> None:
        if book.author not in self._data:
            raise BookNotFoundError
        items = self._data[book.author]
        if book in items:
            items.remove(book)
            if not items:
                del self._data[book.author]
