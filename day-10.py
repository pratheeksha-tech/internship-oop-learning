
# ---------------- BOOK SYSTEM ----------------

class Book:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Book:", self.name)

    def update(self, new_name):
        self.name = new_name

    def delete(self):
        self.name = None


# ---------------- MOBILE SYSTEM ----------------

class Mobile:
    def __init__(self, model):
        self.model = model

    def display(self):
        print("Mobile:", self.model)

    def update(self, model):
        self.model = model

    def delete(self):
        self.model = None


# ---------------- USER SYSTEM ----------------

class User:
    def __init__(self, username):
        self.username = username

    def display(self):
        print("User:", self.username)


# ---------------- CALCULATOR (CALLABLE) ----------------

class Calculator:
    def __call__(self, a, b):
        return a + b


# ---------------- EMPLOYEE (OPERATOR OVERLOADING) ----------------

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __gt__(self, other):
        return self.salary > other.salary


# ---------------- ITERATOR COUNTER ----------------

class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        raise StopIteration


# ---------------- MAIN ----------------

print("=== Book System ===")
b = Book("Python Basics")
b.display()
b.update("Advanced Python")
b.display()

print("\n=== Calculator ===")
calc = Calculator()
print("Sum:", calc(5, 10))

print("\n=== Employee Comparison ===")
e1 = Employee("A", 50000)
e2 = Employee("B", 70000)
print("E2 has higher salary:", e2 > e1)

print("\n=== Counter Iterator ===")
for i in Counter(5):
    print(i)