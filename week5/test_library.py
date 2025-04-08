from book import Book
from library import Library

lib = Library("Test Library")
lib.add_book(Book("Atomic Habits", "James Clear", 2018))
lib.add_book(Book("Deep Work", "Cal Newport", 2016))

# List all books
print("Library Catalog:")
for book in lib.list_books():
    print(book)

# Search and borrow a book
print("\nSearching and borrowing 'Deep WORK'...")
found = lib.find_book("Deep WORK")

if found:
    print(found.borrow())
else:
    print("Book not Found")
