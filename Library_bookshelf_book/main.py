# Define a class for books
class Book:
  def __init__(self, title, author, id_num):
    self.title = title
    self.author = author
    self.id_num = id_num

# Define a class for bookshelves
class Bookshelf:
  def __init__(self):
    self.books = []

  # Method for adding a book to the bookshelf
  def add_book(self, book):
    self.books.append(book)

  # Method for printing the list of books on the bookshelf
  def print_books(self):
    for book in self.books:
      print(book.title, book.author, book.id_num)

# Define a class for libraries
class Library:
  def __init__(self):
    self.bookshelves = []

  # Method for adding a bookshelf to the library
  def add_bookshelf(self, bookshelf):
    self.bookshelves.append(bookshelf)

  # Method for printing the list of books on each bookshelf in the library
  def print_bookshelves(self):
    for bookshelf in self.bookshelves:
      print("Books on bookshelf:")
      bookshelf.print_books()

# Create a library
my_library = Library()

# Create a bookshelf and add it to the library
my_bookshelf = Bookshelf()
my_library.add_bookshelf(my_bookshelf)

# Add a book to the bookshelf
my_book = Book("The Cat in the Hat", "Dr. Seuss", 12345)
my_bookshelf.add_book(my_book)

# Print the list of books on the bookshelf and in the library
my_bookshelf.print_books()
my_library.print_bookshelves()
