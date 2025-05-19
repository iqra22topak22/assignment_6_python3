
# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.


#

class Book:
    total_books = 0  # Class variable

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1  # Class variable ko modify kar rahe hain

# Example: Jab new book add karte hain
Book.increment_book_count()
Book.increment_book_count()
Book.increment_book_count()

print("Total books:", Book.total_books)
# =================================================

class Person:

    @classmethod
    def name(cls):
        name= input("Enter your name :")
        print(f"youer name is {name}")

Person.name()

# ===================================================


