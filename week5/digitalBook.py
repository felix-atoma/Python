from book import Book
class digitalBook(Book):
    def __init__(self, title, author, year, file_size):
       # using super() enherit the properties of the book class
        super().__init__(title, author, year)
        self.file_size = file_size
        
        def stream(self):
            """
            Simulate streaming the digital book.
            """
            return f"Streaming '{self.title}' ({self.file_size}MB)"
        
        def borrow(self):
            """
            Overriding the borrow method to include streaming information.
            """
            if self.available:
                self.available = False
                return f"You have borrowed '{self.title}'. {self.stream()}"
            return f"'{self.title}' is currently NOT available."