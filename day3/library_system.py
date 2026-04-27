# library_system.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.issued_to = None
        self.issued_date = None

    def issue_book(self, student_name, date):
        self.issued_to = student_name
        self.issued_date = date

    def display_book(self):
        print("Title:", self.title)
        print("Author:", self.author)
        if self.issued_to:
            print("Issued To:", self.issued_to)
            print("Issued Date:", self.issued_date)
        else:
            print("Status: Available")


# Example usage
book1 = Book("Python Basics", "Guido van Rossum")
book1.issue_book("Pratheeksha", "2026-04-27")
book1.display_book()