# Part (Book) class
class Book:
    # Can exist independently of the whole
    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self.title

# Whole (Library) Contains Books
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(book.get_title())

# Main function to test aggregation
def main():
    # Creating books
    book1 = Book("To Kill a Mockingbird")
    book2 = Book("1984")

    # Creating a library
    library = Library()

    # Adding books to the library
    library.add_book(book1)
    library.add_book(book2)

    # Displaying books in the library
    library.show_books()

if __name__ == "__main__":
    main()
