from book import Book

class DigitalBook(Book):
    def __init__(self, title, author, year, file_size_mb):
        super().__init__(title, author, year)
        self.file_size_mb = file_size_mb

    def stream(self):
        return f"Streaming '{self.title}' by {self.author}..."

    def borrow(self):
        return f"You can now access '{self.title}' instantly online!"
