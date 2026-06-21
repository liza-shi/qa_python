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
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_success(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1
        assert 'Гордость и предубеждение и зомби' in collector.get_books_genre()


    def test_add_new_book_name_too_long(self):
        collector = BooksCollector()
        long_name = "Жизнь, необыкновенные и удивительные приключения Робинзона Крузо, моряка из Йорка, прожившего ..."
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

   
    def test_add_new_book_empty_name(self):
        collector = BooksCollector()
        collector.add_new_book("")
        assert collector.get_book_genre {}

  
    def test_set_book_genre_success(self):
        collector = BooksCollector
        collector.add_new_book('Гамлет')
        collector.set_book_genre('Гамлет', 'Трагедия')
        assert collector.get_book_genre('Гамлет') == 'Трагедия'

   
    def test_add_book_in_favorites(self):
        collector = BooksCollector
        collector.add_new_book('Гамлет')
        collector.set_book_genre('Гамлет', 'Трагедия')
        collector.add_book_in_favorites('Гамлет')
        assert 'Гамлет' in collector.get_list_of_favorites_books


    def test_delete_book_from_favorites(self):
        collector = BooksCollector
        collector.add_new_book('Гамлет')
        collector.add_book_in_favorites('Гамлет')
        collector.delete_book_from_favorites('Гамлет')
        assert 'Гамлет' not in collector.get_list_of_favorites_books


    def test_get_books_for_children_no_books(self):
        collector = BooksCollector
        assert collector.get_books_for_children == []


    def test_get_books_for_children_only_adult_books(self):
        collector = BooksCollector
        collector.add_new_book('Дракула')
        collector.add_new_book('Внутри убийцы')
        collector.set_book_genre('Дракула', 'Ужас')
        collector.set_book_genre('Внутри убийцы', 'Детектив')
        assert collector.get_books_for_children() == []

  
    def test_add_book_in_favorites_twice(self):
        collector = BooksCollector
        collector.add_new_book('Гамлет')
        collector.add_book_in_favorites('Гамлет')
        collector.add_book_in_favorites('Гамлет')
        assert len(collector.get_list_of_favorites_books()) == 1

    
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector
        collector.add_new_book('Ромэо и Джульета')
        collector.add_new_book('Анна Каренина')
        collector.add_new_book('Поющие в терновнике')
        collector.add_new_book('Гарри Поттер и филосовский камень')
        collector.set_book_genre('Ромэо и Джульета', 'Роман')
        collector.set_book_genre('Анна Каренина', 'Роман')
        collector.set_book_genre('Поющие в терновнике', 'Роман')
        collector.set_book_genre('Гарри Поттер и филосовский камень', 'Фантастика')
        roman_books = collector.get_books_with_specific_genre('Роман')
        assert len(roman_books) == 3
        assert 'Ромэо и Джульета' in roman_books
        assert 'Анна Каренина' in roman_books
        assert 'Поющие в терновнике' in roman_books
        assert 'Гарри Поттер и филосовский камень' not in roman_books



