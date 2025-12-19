class LibraryError(Exception):
    """
    Базовый класс для осталных исключений
    """
    ...

class BookNotFoundError(LibraryError):
    """
    Книга не найдена в коллекции или индексе
    """
    ...

class DuplicateBookError(LibraryError):
    """
    Попытка добавить книгу с уже существующим ISBN
    """
    ...

class LibraryIndexError(LibraryError):
    """
    Ошибка доступа к индексу
    """
    ...

class BookValidationError(LibraryError):
    """
    Некорректный ввод данных книг
    """
    ...
