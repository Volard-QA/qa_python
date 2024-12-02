# Фикстура, созадющая объект класса BooksCollector.
import pytest

from main import BooksCollector

@pytest.fixture (scope='function')
def collector():
    collector = BooksCollector()
    return collector