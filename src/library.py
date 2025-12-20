from src.books.base import BaseBook
from src.collections.author_index import AuthorIndex
from src.collections.book_collection import BookCollection
from src.collections.genre_index import GenreIndex
from src.collections.isbn_index import ISBNIndex
from src.collections.year_index import YearIndex
from src.exceptions import DuplicateBookError


class Library:
    def __init__(self):
        self.books = BookCollection()
        self.isbn_index = ISBNIndex()
        self.author_index = AuthorIndex()
        self.year_index = YearIndex()
        self.genre_index = GenreIndex()
        self._current_pose = 0

    def add_book(self, book: BaseBook) -> None:
        if book.isbn in self.isbn_index:
            raise DuplicateBookError(f'Книга с таким ISBN ({book.isbn}) уже есть в библиотеке')
        self.books.add(book)
        self.isbn_index.add(book)
        self.author_index.add(book)
        self.year_index.add(book)
        self.genre_index.add(book)

    def remove_book(self, book: BaseBook) -> None:
        self.books.remove(book)
        self.isbn_index.remove(book)
        self.author_index.remove(book)
        self.year_index.remove(book)
        self.genre_index.remove(book)

    def find_by_author(self, author: str):
        return self.author_index.get(author, [])

    def find_by_isbn(self, isbn: str):
        return self.isbn_index.get(isbn, None)

    def find_by_year(self, year: int):
        return self.year_index.get(year, [])

    def find_by_genre(self, genre: str):
        return self.genre_index.get(genre, [])

    def __len__(self) -> int:
        return len(self.books)

    def __iter__(self):
        self._current_pose = 0
        return self

    def __next__(self) -> BaseBook:
        if self._current_pose < len(self.books):
            book = self.books[self._current_pose]
            self._current_pose += 1
            return book
        else:
            self._current_pose = 0
            raise StopIteration

    def __getitem__(self, index: int | slice):
        if isinstance(index, slice):
            return Library(self.books[index])
        return self.books[index]
