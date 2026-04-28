from abc import ABC, abstractmethod

# ---------------- ABSTRACTION ----------------

class System(ABC):
    @abstractmethod
    def run(self):
        pass


# ---------------- LIBRARY MANAGEMENT ----------------

class Library(System):
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __str__(self):   # dunder method
        return f"Library contains: {', '.join(self.books)}"

    def run(self):
        print("Library System Running")


# ---------------- STUDENT SYSTEM ----------------

class Student:
    school_name = "Global Academy"
    count = 0

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        Student.count += 1

    @classmethod
    def total_students(cls):
        return cls.count

    @staticmethod
    def grade(marks):
        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        elif marks >= 50:
            return "C"
        else:
            return "Fail"

    def __str__(self):
        return f"{self.name} - {self.marks}"


# ---------------- DECORATOR (SECURITY SYSTEM) ----------------

def access_control(func):
    def wrapper(user):
        if user == "admin":
            return func(user)
        else:
            return "Access Denied"
    return wrapper


@access_control
def dashboard(user):
    return "Secure Dashboard Access Granted"


# ---------------- MAIN PROGRAM ----------------

print("=== Library System ===")
lib = Library()
lib.add_book("Python Basics")
lib.add_book("OOP Concepts")
print(lib)
lib.run()

print("\n=== Student System ===")
s1 = Student("Pratheeksha", 88)
s2 = Student("Rahul", 72)

print(s1)
print(s2)
print("Total Students:", Student.total_students())
print("Grade:", Student.grade(88))

print("\n=== Security System ===")
print(dashboard("admin"))
print(dashboard("user"))