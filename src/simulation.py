import random
from src.books.audio_book import AudioBook
from src.books.base import BaseBook
from src.books.electronic_book import EBook
from src.books.printed_book import PrintedBook
from src.constants import AUTHORS, EBOOK_FORMATS, GENRES, NARRATORS, TITLES, YEARS
from src.exceptions import BookValidationError, LibraryError, LibraryIndexError
from src.library import Library
from src.setup_logger import logger


def generate_random_book() -> BaseBook:
    """
    Генерирует книгу рандомного типа и заполняет необходимые поля конструктора рандомными(осмысленными) значениями

    :return: Сгенерированная книга
    :rtype: BaseBook
    """
    title = random.choice(TITLES)
    author = random.choice(AUTHORS)
    year = random.choice(YEARS)
    genre = random.choice(GENRES)
    isbn = f'{random.randint(100, 999)}-{random.randint(1000, 9999)}'

    type_choice = random.choice(['printed', 'audio', 'ebook'])

    match type_choice:
        case 'audio':
            return AudioBook(title, author, year, genre, isbn,
                             duration=random.randint(30, 5000),
                             bitrate=random.choice([32, 128, 256]),
                             narrator=random.choice(NARRATORS))
        case 'ebook':
            return EBook(title, author, year, genre, isbn,
                         file_size=random.uniform(1.0, 50.0),
                         file_format=random.choice(EBOOK_FORMATS))
        case 'printed':
            return PrintedBook(title, author, year, genre, isbn,
                               pages_count=random.randint(100, 1000),
                               weight=random.randint(200, 1500))
        case _:
            return PrintedBook(title, author, year, genre, isbn,
                               pages_count=random.randint(100, 1000),
                               weight=random.randint(200, 1500))

def run_simulation(steps: int = 20, seed: int | None = None) -> None:
    """
    Выполняет псевдослучайную симуляцию

    :param steps: Количество шагов симуляции
    :type steps: int
    :param seed: Seed для псевдослучайной генерации
    :type seed: int | None
    """
    if seed is not None:
        random.seed(seed)

    lib = Library()

    text = f'Начало симуляции (steps: {steps}, seed: {seed})'
    print(text)
    logger.info(text)
    for i in range(random.randint(3, 11)):
        try:
            lib.add_book(generate_random_book())
        except BookValidationError as e:
            print(f'Не удалось добавить книгу: {e}')
    actions = ['add', 'remove', 'search_by_author', 'search_by_genre', 'search_by_year', 'fail_isbn',
                'add_duplicate', 'update_index']
    print('Начальное состояние библиотеки:')
    for book in lib:
        print(f'- {book}')
    print('-'*64)
    for step in range(1, steps + 1):
        action = random.choice(actions)
        print(f'{step:02d}. {action.upper():<16} | ', end='')
        text = f'{action.upper()} | '
        try:
            match action:
                case 'add':
                    book = generate_random_book()
                    lib.add_book(book)
                    text += f'OK. Добавлена {book}'
                    print(f'OK. Добавлена {book}')
                    logger.info(text)

                case 'remove':
                    if len(lib) > 0:
                        index = random.randint(0, len(lib) - 1)
                        book = lib.books[index]
                        lib.remove_book(book)
                        text += f'OK. Удалена {book}'
                        print(f'OK. Удалена {book}')
                        logger.info(text)
                    else:
                        text += 'FAILED. Удаление не удалось. Библиотека пуста'
                        print('FAILED. Удаление не удалось. Библиотека пуста')
                        logger.warning(text)

                case 'search_by_genre':
                    genre = random.choice(GENRES)
                    result = lib.find_by_genre(genre)
                    text += f'OK. Поиск по жанру "{genre}": найдено {len(result)}'
                    print(f'OK. Поиск по жанру "{genre}": найдено {len(result)}')
                    logger.info(text)

                case 'search_by_author':
                    author = random.choice(AUTHORS)
                    result = lib.find_by_author(author)
                    text += f'OK. Поиск по автору "{author}": найдено {len(result)}'
                    print(f'OK. Поиск по автору "{author}": найдено {len(result)}')
                    logger.info(text)

                case 'search_by_year':
                    year = random.choice(YEARS)
                    result = lib.find_by_year(year)
                    text += f'OK. Поиск по {year} году: найдено {len(result)}'
                    print(f'OK. Поиск по {year} году: найдено {len(result)}')
                    logger.info(text)

                case 'fail_isbn':
                    fake_isbn = '666-FAIL'
                    text += f'Проверка вызова ISBN {fake_isbn}: '
                    print(f'Проверка вызова ISBN {fake_isbn}: ', end='')
                    _ = lib.isbn_index[fake_isbn]

                case 'update_index':
                    if len(lib) > 0:
                        target = random.choice(lib.books)
                        lib.remove_book(target)
                        target.year = random.choice(YEARS)
                        lib.add_book(target)
                        text += f'OK. Индекс {target} обновлен'
                        print(f'OK. Индекс {target} обновлен')
                        logger.info(text)
                    else:
                        text += 'SKIPPED. Библиотека пуста'
                        print('SKIPPED. Библиотека пуста')
                        logger.warning(text)

                case 'add_duplicate':
                    if len(lib) > 0:
                        existing_book = lib.books[0]
                        text += f'Попытка добавить дубликат (ISBN: {existing_book.isbn}) '
                        print(f'Попытка добавить дубликат (ISBN: {existing_book.isbn}) ', end='')
                        lib.add_book(existing_book)
                    else:
                        text += 'Библиотека пуста. Тест пропущен'
                        print('Библиотека пуста. Тест пропущен')
                        logger.warning(text)
        except LibraryIndexError:
            text += 'Ошибка: Книга с таким ключом отсутствует в системе'
            print(text)
            logger.error(text)
        except BookValidationError as e:
            text += f'Ошибка валидации: {e}'
            print(text)
            logger.error(text)
        except LibraryError as e:
            text += f'Системная ошибка: {e}'
            print(text)
            logger.error(text)
        except Exception as e:
            text += f'Непредвиденная ошибка: {e}'
            print(text)
            logger.error(text)
    text = f'Конец симуляции. Всего книг: {len(lib)}'
    print(text)
    logger.info(text)
    print('Библиотека:')
    if len(lib) > 1:
        print_slice = [book for book in lib.books[0:2]]
        for book in print_slice:
            print(book)
        for book in lib.books[2:]:
            print(book)
    elif len(lib) == 1:
        print(lib[0])
