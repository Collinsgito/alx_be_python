# book_class.py

class Book:
    def __init__(self, title, author, year):
        """Constructor to initialize the book's title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor to indicate when the object is being deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """User-friendly string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Developer-friendly representation that could recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
