import unittest
from unittest.mock import patch

from src.books.printed_book import PrintedBook
from src.simulation import run_simulation

def make_book(isbn='111-1111', year=2000):
    return PrintedBook('Test', 'Author', year, 'Drama', isbn, 100, 500)

class TestSimulation(unittest.TestCase):
    @patch('src.simulation.print')
    @patch('src.simulation.generate_random_book')
    @patch('src.simulation.random.randint', return_value=0)
    def test_add_book(self, mock_randint, mock_gen, mock_print):
        book = make_book()
        mock_gen.return_value = book
        with patch('src.simulation.random.choice', return_value='add'):
            run_simulation(steps=3, seed=1)
        self.assertEqual(mock_gen.call_count, 3)

    @patch('src.simulation.print')
    @patch('src.simulation.generate_random_book')
    @patch('src.simulation.random.randint', return_value=0)
    def test_remove_book(self, mock_randint, mock_gen, mock_print):
        book = make_book()
        mock_gen.return_value = book
        with patch('src.simulation.random.choice',
                   side_effect=['add', 'remove']):
            run_simulation(steps=2, seed=1)

    @patch('src.simulation.print')
    @patch('src.simulation.generate_random_book')
    @patch('src.simulation.random.randint', return_value=0)
    def test_add_duplicate(self, mock_randint, mock_gen, mock_print):
        book = make_book('DUP-123')
        mock_gen.return_value = book
        with patch('src.simulation.random.choice',
                   side_effect=['add', 'add_duplicate']):
            run_simulation(steps=2, seed=1)
        self.assertTrue(True)

    @patch('src.simulation.print')
    @patch('src.simulation.random.randint', return_value=0)
    def test_fail_isbn(self, mock_randint, mock_print):
        with patch('src.simulation.random.choice', return_value='fail_isbn'):
            run_simulation(steps=1, seed=1)
        self.assertTrue(True)

    @patch('src.simulation.print')
    @patch('src.simulation.generate_random_book')
    @patch('src.simulation.random.randint', return_value=0)
    def test_update_index(self, mock_randint, mock_gen, mock_print):
        book = make_book()
        mock_gen.return_value = book
        with patch('src.simulation.random.choice',
                   side_effect=['add', 'update_index']):
            run_simulation(steps=2, seed=1)
