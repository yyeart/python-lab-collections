from src.books.printed_book import PrintedBook
from src.collections.author_index import AuthorIndex
from src.collections.book_collection import BookCollection
from tests.fixtures import sample_printed_book, sample_ebook
from src.collections.isbn_index import ISBNIndex

def test_book_collection_slice(sample_printed_book, sample_ebook):
    coll = BookCollection([sample_printed_book, sample_ebook])
    sliced = coll[0:1]
    assert isinstance(sliced, BookCollection)
    assert len(sliced) == 1
    assert sliced[0] == sample_printed_book

def test_book_collection_index(sample_printed_book, sample_ebook):
    isbn_index = ISBNIndex()
    author_index = AuthorIndex()
    book1 = PrintedBook("Book1", 'Author1', 2000, 'Genre', '123-1234', 100, 100)
    book2 = PrintedBook("Book2", 'Author1', 2001, 'Genre', '123-1211', 100, 100)
    for b in [book1, book2]:
        isbn_index.add(b)
        author_index.add(b)
    assert len(isbn_index) == 2
    assert len(author_index['Author1']) == 2
    author_index.remove(book1)
    assert len(author_index['Author1']) == 1
