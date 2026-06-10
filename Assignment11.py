from abc import ABC, abstractmethod


class LibraryItem(ABC):

    total_items = 0

    def __init__(self, title, year):
        self.title = title
        self.year = year
        LibraryItem.total_items += 1

    @abstractmethod
    def displayInfo(self):
        pass

    @staticmethod
    def getTotalItems():
        return LibraryItem.total_items


class Book(LibraryItem):

    # Default argument demonstrates constructor overloading
    def __init__(self, title, year, author="Unknown Author"):
        super().__init__(title, year)
        self.author = author

    def displayInfo(self):
        print("Book Details:")
        print(f"Title  : {self.title}")
        print(f"Author : {self.author}")
        print(f"Year   : {self.year}")


class DVD(LibraryItem):

    # Default argument demonstrates constructor overloading
    def __init__(self, title, year, duration, genre="General"):
        super().__init__(title, year)
        self.duration = duration
        self.genre = genre

    def displayInfo(self):
        print("DVD Details:")
        print(f"Title    : {self.title}")
        print(f"Genre    : {self.genre}")
        print(f"Duration : {self.duration} minutes")
        print(f"Year     : {self.year}")


book1 = Book("The Alchemist", 1988, "Paulo Coelho")
book2 = Book("Python Basics", 2020)

dvd1 = DVD("Inception", 2010, 148, "Sci-Fi")
dvd2 = DVD("The Lion King", 1994, 88)

# Polymorphism using a collection of LibraryItem objects
library = [book1, book2, dvd1, dvd2]

print("Library Items:\n")

for item in library:
    item.displayInfo()
    print()

print(f"Total Library Items Created: {LibraryItem.getTotalItems()}")