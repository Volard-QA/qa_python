import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test

class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        # создаем экземпляр (объект) класса BooksCollector - объект создается фикстурой.
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    #Проверяем добавление дублей книг
    @pytest.mark.parametrize('book_name', ['Лабиринты Эхо', 'Вишневый сад', 'Цифровое искусство'])
    def test_add_new_book_not_add_same_book(self, collector, book_name):
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)

        assert len(collector.get_books_genre()) == 1

    #Проверяем соответствие жанра, который записали тому, который должны были записать
    @pytest.mark.parametrize('book_name, genre', [['Лабиринты Эхо','Фантастика'],
                                                  ['Операция Ы','Комедия'],
                                                  ['Душа','Мультфильм']])
    def test_set_book_genre_set_genre_correctly(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)

        assert collector.books_genre[book_name] == genre

    #Проверяем соответствие выводимого функцией жанра установленному.
    @pytest.mark.parametrize('book_name, expected_genre', [['Лабиринты Эхо', 'Фантастика']])

    def test_get_book_genre_get_set_genre_correctly(self, collector, book_name, expected_genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, expected_genre)

        assert collector.get_book_genre(book_name) == expected_genre

    # Для проверки, что формируется список именно конкретного выбранного жанра - добавлена третья книга, другим относительно запрашиваемого жанром
    @pytest.mark.parametrize('book_1_name, book_2_name, book_3_name', [['Лабиринты Эхо',
                                                           'Остров сокровищ', 'Хроники Нарнии']])

    def test_get_books_with_specific_genre_return_valid_book_names(self, collector, book_1_name, book_2_name, book_3_name):
        collector.add_new_book(book_1_name)
        collector.set_book_genre(book_1_name, 'Фантастика')
        collector.add_new_book(book_2_name)
        collector.set_book_genre(book_2_name, 'Мультфильмы')
        collector.add_new_book(book_3_name)
        collector.set_book_genre(book_3_name, 'Фантастика')

        assert collector.get_books_with_specific_genre('Фантастика') == [book_1_name, book_3_name]

    #Проверяем корректное создание словаря книг с жанрами
    def test_get_books_genre_get_correct_dic_data(self, collector):
        collector.add_new_book('Лабиринты Эхо')
        collector.set_book_genre('Лабиринты Эхо', 'Фантастика')
        collector.add_new_book('Душа')
        collector.set_book_genre('Душа', 'Мультфильмы')

        assert collector.get_books_genre() == {'Лабиринты Эхо': 'Фантастика', 'Душа': 'Мультфильмы'}

    # Проверяем, что функция get_books_for_children не возвращает книги из списка возрастного рейтинга
    @pytest.mark.parametrize('children_book_name, adult_book_name_1, adult_book_name_2', [
        ['Остров сокровищ', 'Лабиринты Эхо', 'Психо']])

    def test_get_books_for_children_not_get_books_with_genre_age_rating(self, collector, children_book_name,adult_book_name_1, adult_book_name_2):
        collector.add_new_book(children_book_name)
        collector.set_book_genre(children_book_name, 'Мультфильмы')
        collector.add_new_book(adult_book_name_1)
        collector.set_book_genre(adult_book_name_1, 'Детективы')
        collector.add_new_book(adult_book_name_2)
        collector.set_book_genre(adult_book_name_2, 'Ужасы')

        assert collector.get_books_for_children() == [children_book_name]

    # Проверяем, что книгу можно добавить в избранное
    @pytest.mark.parametrize('book_name', ['Лабиринты Эхо'])

    def test_add_book_in_favorites_books_added_successful(self, collector, book_name):
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)

        assert book_name in collector.favorites

    #Проверяем невозможность повторного добавления книги в избранное
    @pytest.mark.parametrize('book_name', ['Лабиринты Эхо'])

    def test_add_book_in_favorites_books_doubles_not_added(self, collector, book_name):
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        initial_favorites_count = len(collector.favorites) #Сохраняю количество книг в избранном после первого добавления
        collector.add_book_in_favorites(book_name)

        assert len(collector.favorites) == initial_favorites_count

    # Проверяем корректное удаление книги из избранного
    @pytest.mark.parametrize('book_name', ['Лабиринты Эхо'])

    def test_delete_book_from_favorites_book_removed_from_favorites(self, collector, book_name):
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)

        assert book_name not in collector.favorites

    # Проверяем корректный вывод списка книг в избранном
    def test_get_list_of_favorites_books_got_expected_books(self, collector):
        collector.add_new_book('Лабиринты Эхо')
        collector.add_book_in_favorites('Лабиринты Эхо')
        collector.add_new_book('Приключения капитан Гранта')
        collector.add_book_in_favorites('Приключения капитан Гранта')

        assert collector.get_list_of_favorites_books() == ['Лабиринты Эхо', 'Приключения капитан Гранта']
