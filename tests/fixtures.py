import pytest # type: ignore

from src.books.electronic_book import EBook
from src.books.printed_book import PrintedBook
from src.library import Library

@pytest.fixture
def sample_printed_book():
    return PrintedBook("1984", "Джордж Оруэлл", 1949, "Антиутопия", "111-2222", 500, 400)

@pytest.fixture
def sample_ebook():
    return EBook("Преступление и наказание", "Фёдор Достоевский", 1866, "Психологический роман", "222-3333",
                 2.5, 'PDF')

@pytest.fixture
def library():
    return Library()
