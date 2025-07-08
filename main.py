class Book:
    def __init__(self, title, author, year, id):
        self.title = title
        self.author = author
        self.year = year
        self.id = id
    
    def display_info(self):
        print(f"Назва: {self.title}, Автор: {self.author}, Рік видання: {self.year}, id: {self.id}")


class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"Книгу '{book.title}' додано до бібліотеки.")
    
    def remove_book(self, id):
        for book in self.books:
            if book.id == id:
                self.books.remove(book)
                print(f"Книгу з id {id} видалено з бібліотеки.")
                return
        print(f"Книгу з id {id} не знайдено.")
    
    def find_book_by_title(self, title):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]
        if found_books:
            print(f"Знайдено {len(found_books)} книг з назвою '{title}':")
            for book in found_books:
                book.display_info()
        else:
            print(f"Книг з назвою '{title}' не знайдено.")
        return found_books
    
    def display_all_books(self):
        if not self.books:
            print("Бібліотека порожня.")
            return
        
        print("Книги в бібліотеці:")
        for book in self.books:
            book.display_info()


# Створення екземплярів книг
book1 = Book("Гаррі Поттер і філософський камінь", "Дж. К. Роулінг", 1997, 1)
book2 = Book("Володар перснів: Братство персня", "Дж. Р. Р. Толкін", 1954, 2)
book3 = Book("1984", "Джордж Орвелл", 1949, 3)
book4 = Book("Гаррі Поттер і таємна кімната", "Дж. К. Роулінг", 1998, 4)

# Створення бібліотеки та додавання книг
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

# Виведення всіх книг
print("\nВсі книги в бібліотеці:")
library.display_all_books()

# Пошук книги за назвою
print("\nПошук книг:")
library.find_book_by_title("1984")
library.find_book_by_title("Гаррі Поттер")

# Видалення книги
print("\nВидалення книги:")
library.remove_book(2)

# Виведення всіх книг після видалення
print("\nОновлений список книг:")
library.display_all_books()