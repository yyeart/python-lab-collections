import pytest # type: ignore
from src.exceptions import BookNotFoundError, DuplicateBookError
from tests.fixtures import sample_printed_book, library, sample_ebook

def test_library_add_duplicate(library, sample_printed_book):
    library.add_book(sample_printed_book)
    with pytest.raises(DuplicateBookError):
        library.add_book(sample_printed_book)

def test_library_remove_nonexistent(library, sample_printed_book):
    with pytest.raises(BookNotFoundError):
        library.remove_book(sample_printed_book)

def test_library_iterator(library, sample_printed_book, sample_ebook):
    library.add_book(sample_ebook)
    library.add_book(sample_printed_book)
    books = []
    for book in library:
        books.append(book)

    assert len(books) == 2
    assert books[0].isbn == '222-3333'

def test_library_search(library, sample_ebook, sample_printed_book):
    library.add_book(sample_printed_book)
    library.add_book(sample_ebook)

    assert len(library.find_by_author('Джордж Оруэлл')) == 1
    assert len(library.find_by_author('unknown')) == 0

    assert len(library.find_by_genre("Антиутопия")) == 1
    assert len(library.find_by_genre('unknown')) == 0

    assert len(library.find_by_year(1949)) == 1
    assert len(library.find_by_year(123)) == 0

    assert library.find_by_isbn('111-2222') == sample_printed_book
