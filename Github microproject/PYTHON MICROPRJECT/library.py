from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        self.issued_to = None
        self.due_date = None

    def __str__(self):
        status = "Available" if self.available else f"Issued to {self.issued_to} (Due: {self.due_date.strftime('%Y-%m-%d') if self.due_date else 'N/A'})"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {status}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn):
        if any(book.isbn == isbn for book in self.books):
            return False  # ISBN already exists
        book = Book(title, author, isbn)
        self.books.append(book)
        return True

    def issue_book(self, isbn, user, days=14):
        for book in self.books:
            if book.isbn == isbn and book.available:
                book.available = False
                book.issued_to = user
                book.due_date = datetime.now() + timedelta(days=days)
                return True
        return False

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.available:
                book.available = True
                book.issued_to = None
                book.due_date = None
                return True
        return False

    def search_books(self, query):
        return [book for book in self.books if query.lower() in book.title.lower() or query.lower() in book.author.lower()]

    def list_available_books(self):
        return [book for book in self.books if book.available]

    def list_issued_books(self):
        return [book for book in self.books if not book.available]

    def check_overdue(self):
        now = datetime.now()
        overdue = []
        for book in self.books:
            if not book.available and book.due_date and book.due_date < now:
                overdue.append(book)
        return overdue

    def calculate_fine(self, isbn, fine_per_day=1.0):
        for book in self.books:
            if book.isbn == isbn and not book.available and book.due_date:
                now = datetime.now()
                if book.due_date < now:
                    days_overdue = (now - book.due_date).days
                    return days_overdue * fine_per_day
        return 0.0