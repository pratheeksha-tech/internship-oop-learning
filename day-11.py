
# ---------------- BASE CLASS ----------------

class Profile:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        return f"{self.role}: {self.name}"


# ---------------- SCHOOL SYSTEM ----------------

class School(Profile):
    def __init__(self, name, role, subject):
        super().__init__(name, role)
        self.subject = subject

    def display(self):
        return f"{super().display()} | Subject: {self.subject}"


# ---------------- VEHICLE SYSTEM ----------------

class Vehicle:
    def __init__(self, vtype, number):
        self.vtype = vtype
        self.number = number

    def display(self):
        return f"{self.vtype} - {self.number}"


# ---------------- EMPLOYEE SYSTEM ----------------

class Employee(Profile):
    def __init__(self, name, role, salary):
        super().__init__(name, role)
        self.salary = salary

    def display(self):
        return f"{super().display()} | Salary: {self.salary}"


# ---------------- LIBRARY SYSTEM ----------------

class Book:
    def __init__(self, title, category):
        self.title = title
        self.category = category

    def display(self):
        return f"{self.title} ({self.category})"


# ---------------- ONLINE LEARNING SYSTEM ----------------

class User(Profile):
    def __init__(self, name, role, course):
        super().__init__(name, role)
        self.course = course

    def display(self):
        return f"{super().display()} | Course: {self.course}"


# ---------------- MAIN ----------------

print("=== School System ===")
s = School("Pratheeksha", "Student", "Python")
print(s.display())

print("\n=== Vehicle System ===")
v = Vehicle("Car", "KA01AB1234")
print(v.display())

print("\n=== Employee System ===")
e = Employee("Rahul", "Developer", 50000)
print(e.display())

print("\n=== Library System ===")
b = Book("OOP Concepts", "Programming")
print(b.display())

print("\n=== Learning Platform ===")
u = User("Anita", "Learner", "Machine Learning")
print(u.display())