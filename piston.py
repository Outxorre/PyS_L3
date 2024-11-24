class Yaitso:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f"Hello, Im {self.name}")

class Auto:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def show_passengers(self):
        if self.passengers:
            for i in self.passengers:
                print(f"Passenger: {i.name}")
        else:
            print("Passenger List is empty")

mercebowles = Auto("Mosrodes","Balbes99", "2088")
human1 = Yaitso("Nurbekzhan", 4)
human2 = Yaitso("Balbes32", 9)

mercebowles.add_passenger(human1)
mercebowles.add_passenger(human2)

mercebowles.show_passengers()




#Задание 1


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def bookInfo(self):
        print(f"Название книги: {self.title}, Автор: {self.author}")

book1 = Book("Bulba", "Anchovy")
book2 = Book("Bulba2", "Anchovy2")
book1.bookInfo()

#Задание 2
class Reader:
    def __init__(self,name):
        self.name = name
        self.borrowedBooks = []

    def borrowBook(self, book):
        self.borrowedBooks.append(book)

    def returnBook(self, book):
        for book in self.borrowedBooks:
            self.borrowedBooks.remove(book)
            print(f"{book.title} Успешно возвращена")

        else:
            print("Не найдено в массиве")
        # for i in self.borrowedBooks:
        #     self.borrowedBooks.remove(i)

    def showBooks(self):
        if self.borrowedBooks:
            for i in self.borrowedBooks:
                print(f"Book: {i.title}")
        else:
            print("Books List is empty")

reader1 = Reader("Nuradil")
reader1.borrowBook(book1)
reader1.borrowBook(book2)

reader1.showBooks()

print("")


reader1.returnBook(book1)

print("")

reader1.showBooks()

#Задание 3
class Library:
    def __init__(self, books = [], readers = []):
        self.books = books
        self.readers = readers

    def add_book(self, book):
        self.books.append(book)

    def add_reader(self, reader):
        self.readers.append(reader)

    def lend_book(self, book, reader):
        if book in self.books:
            self.books.remove(book)
            reader.returnBook(book)

        else:
            print(f"book {book.title} not found")

    def show_books(self):
        if self.books:
            print("Books:")
            for book in self.books:
                print(f"{book.title}")
            else:
                print("Not found")

    def show_readers(self):
        if self.readers:
            print("Readers:")
            for reader in self.readers:
                print(f"{reader.title}")
            else:
                print("Not found")
п
