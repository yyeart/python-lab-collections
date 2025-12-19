import pytest # type: ignore
from src.books.audio_book import AudioBook
from src.books.electronic_book import EBook
from src.books.printed_book import PrintedBook
from src.simulation import generate_random_book, run_simulation


def test_generate_random_book():
    book = generate_random_book()
    assert isinstance(book, (AudioBook, EBook, PrintedBook))

def test_simulation_run():
    try:
        run_simulation(steps=50, seed=1)
    except Exception as e:
        pytest.fail(str(e))
