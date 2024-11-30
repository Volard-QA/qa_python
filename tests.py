import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    #Проверяем добавление дублей книг
    import pytest
    @pytest.mark.parametrize('book_name', ['Лабиринты Эхо', 'Вишневый сад', 'Цифровое искусство'])
    def test_add_new_book_add_same_book(book_name):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1

    #Проверяем соответствие жанра, который записали тому, который должны были записать
    @pytest.mark.parametrize('book_name, genre', [['Лабиринты Эхо','Фантастика'],
                                                  ['Операция Ы','Комедия'],
                                                  ['Душа','Мультфильм']])
    def test_set_book_genre_set_genre_correctly(book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.books_genre[book_name] == genre

    #Проверяем соответствие выводимого функцией жанра установленному.
    @pytest.mark.parametrize('book_name, genre', [['Лабиринты Эхо', 'Фантастика']])

    def test_get_book_genre_get_set_genre_correctly(book_name, expected_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, expected_genre)
        assert collector.get_book_genre(book_name) == expected_genre

    @pytest.mark.parametrize('book_1_name, book_2_name', [['Лабиринты Эхо',
                                                           'Хроники Нарнии']])

    def test_get_books_with_specific_genre_return_valid_book_names(book_1_name,book_2_name):
        collector = BooksCollector()
        collector.add_new_book(book_1_name)
        collector.set_book_genre(book_1_name, 'Фантастика')
        collector.add_new_book(book_2_name)
        collector.set_book_genre(book_2_name, 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == [book_1_name, book_2_name]

    #Проверяем корректное создание словаря книг с жанрами
    def test_get_books_genre_get_correct_dic_data(self):
        collector = BooksCollector()
        collector.add_new_book('Лабиринты Эхо')
        collector.set_book_genre('Лабиринты Эхо', 'Фантастика')
        collector.add_new_book('Душа')
        collector.set_book_genre('Душа', 'Мультфильмы')

        assert collector.get_books_genre() == {'Лабиринты Эхо': 'Фантастика', 'Душа': 'Мультфильмы'}

    # Проверяем, что функция get_books_for_children не возвращает книги из списка возрастного рейтинга
    @pytest.mark.parametrize('book_name, genre', [['Лабиринты Эхо','Детективы'],
                                                  ['Психо','Ужасы']]
                             )

    def test_get_books_for_children_not_get_books_with_genre_age_rating(book_name,genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        collector.get_books_genre(book_name, genre)

        assert collector.get_books_for_children() == []

    # Проверяем, что книгу можно добавить в избранное
    @pytest.mark.parametrize('book_name', ['Лабиринты Эхо'])

    def test_add_book_in_favorites_books_added_successful(book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)

        assert book_name in collector.favorites

    #Проверяем невозможность повторного добавления книги в избранное
    @pytest.mark.parametrize('book_name', ['Лабиринты Эхо'])

    def test_add_book_in_favorites_books_doubles_not_added(book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        initial_favorites_count = len(collector.favorites) #Сохраняю количество книг в избранном после первого добавления
        collector.add_book_in_favorites(book_name)

        assert len(collector.favorites) == initial_favorites_count

    # Проверяем корректное удаление книги из избранного
    @pytest.mark.parametrize('book_name', ['Лабиринты Эхо'])

    def test_delete_book_from_favorites_book_removed_from_favorites(book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)

        assert book_name not in collector.favorites

    # Проверяем корректный вывод списка книг в избранном
    def test_get_list_of_favorites_books_got_expected_books(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Лабиринты Эхо')
        collector.add_book_in_favorites('Приключения капитан Гранта')

        assert collector.get_list_of_favorites_books() == ['Лабиринты Эхо', 'Приключения капитан Гранта']