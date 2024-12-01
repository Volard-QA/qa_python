# qa_python Sprint 4
# Описание тестов на main.
# 1) Демонстрационный тест проверяет возможность добавить две книги в словарь books_rating
# 2) Тест test_add_new_book_not_add_same_book проверяет невозможность методом add_new_book добавить дубли книг в словарь books_rating.
# 3) Тест test_set_book_genre_set_genre_correctly проверяет соответствие добавленного жанра книги тому, который мы добавляли методом set_book_genre.
# 4) Тест test_get_book_genre_get_set_genre_correctly проверяет корректность работы метода get_book_genre - он должен вернуть тот жанр книги, который был задан методом set_book_genre.
# 5) Тест test_get_books_with_specific_genre_return_valid_book_names  проверяет корректность выборки книг определенного жанра, возвращаемого функцией get_books_with_specific_genre.
# 6) Тест test_get_books_genre_get_correct_dic_data проверяет корректность создания справочника books_genre.
# 7) Тест test_get_books_for_children_not_get_books_with_genre_age_rating проверяет, что метод get_books_for_children не добавляет в выборку книг книги с возрастным рейтингом из списка genre_age_rating.
# 8) Тест test_add_book_in_favorites_books_added_successful проверяет корректное добавление книг в список favorites функцией add_book_in_favorites.
# 9) Тест test_add_book_in_favorites_books_doubles_not_added проверяет невозможность добавить дубли ниг в список favorites функцией add_book_in_favorites.
# 10) Тест test_delete_book_from_favorites_book_removed_from_favorites проверяет корректное удаление книг из списка favorites функцией delete_book_from_favorites.
# 11) Тест test_get_list_of_favorites_books_got_expected_books проверяет, что метод get_list_of_favorites_books выводит корректный перечень книг, добавленных в список favorites.