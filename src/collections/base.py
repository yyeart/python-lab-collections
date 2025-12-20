from abc import ABC, abstractmethod
from typing import Any
from src.books.base import BaseBook
from src.exceptions import LibraryIndexError

class BaseIndex(ABC):
    """
    Абстрактный базовый класс для реализации словарных коллекций индексов
    """
    def __init__(self):
        self._data = {}

    @abstractmethod
    def add(self, book: BaseBook) -> None:
        ...

    @abstractmethod
    def remove(self, book: BaseBook) -> None:
        ...

    def __getitem__(self, key: Any) -> BaseBook | list[BaseBook]:
        try:
            return self._data[key]
        except KeyError:
            raise LibraryIndexError(f'Ключ "{key}" отсутствует в индексе')

    def __contains__(self, key: Any) -> bool:
        return key in self._data

    def __len__(self) -> int:
        return len(self._data)

    def get(self, key: Any, default=None):
        return self._data.get(key, default)
