class Book:
    def __init__(self, title, author, year):
        """
        Constructor method to initialize the book object
        """
        self.title = title
        self.author = author
        self.year = year
        self.available = True  # Default to available

    def borrow(self):
        """
        Marks the book as borrowed if the book is available
        """
        if self.available:
            self.available = False
            return f"You have borrowed '{self.title}'."
        return f"'{self.title}' is currently NOT available."

    def return_book(self):
        """
        Marks the book as returned
        """
        self.available = True
        return f"'{self.title}' has been returned."

    def get_details(self):
        """
        Returns formatted book information.
        """
        status = "Available" if self.available else "Checked out"
        return f"{self.title} by {self.author} ({self.year}) - {status}"
