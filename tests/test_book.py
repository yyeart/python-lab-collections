import pytest # type: ignore
from tests.fixtures import sample_printed_book
from src.books.audio_book import AudioBook
from src.books.printed_book import PrintedBook
from src.exceptions import BookValidationError

def test_book_validation():
    with pytest.raises(BookValidationError):
        PrintedBook('bad', 'book', -100, 'example', '666-6666', 15, 15)

    with pytest.raises(BookValidationError):
        AudioBook('bad', 'audiobook', 2000, 'example', '123-1234', -15, 128, 'AI')

def test_book_equal(sample_printed_book):
    same_book = PrintedBook("1984", "Джордж Оруэлл", 1949, "Антиутопия", "111-2222", 500, 400)
    assert same_book == sample_printed_book
    assert hash(same_book) == hash(sample_printed_book)
