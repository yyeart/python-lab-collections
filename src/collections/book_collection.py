from src.books.base import BaseBook
from src.exceptions import BookNotFoundError, LibraryIndexError
from typing import Iterator

class BookCollection:
    def __init__(self, items: list[BaseBook] | None = None):
        self._data: list[BaseBook] = items if items is not None else []

    def add(self, book: BaseBook) -> None:
        self._data.append(book)

    def remove(self, book: BaseBook) -> None:
        if book in self._data:
            self._data.remove(book)
        else:
            raise BookNotFoundError(f'Книга "{book.title}" (ISBN: {book.isbn}) не найдена')

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self) -> Iterator[BaseBook]:
        return iter(self._data)

    def __getitem__(self, index: int | slice):
        if isinstance(index, slice):
            return BookCollection(self._data[index])
        try:
            return self._data[index]
        except IndexError:
            raise LibraryIndexError('Индекс книги выходит за границы коллекции')

    def __repr__(self) -> str:
        return f'BookCollection ({len(self)} books)'
