from abc import ABC, abstractmethod

# ---------------- GRADING SYSTEM ----------------

class GradeSystem:
    def __init__(self):
        self.grade = 0

    def update_grade(self, new_grade):
        if new_grade > self.grade:
            self.grade = new_grade

    def get_grade(self):
        return self.grade


# ---------------- TIME TRACKING ----------------

class TimeTracker:
    def __init__(self):
        self.count = 0

    def log_access(self):
        self.count += 1
        return self.count


# ---------------- LIBRARY SYSTEM ----------------

class Book:
    def __init__(self, title):
        self.title = title


# ---------------- ABSTRACT WINDOW SYSTEM ----------------

class Window(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class SquareWindow(Window):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side


class RectangleWindow(Window):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def calculate_area(self):
        return self.l * self.b


# ---------------- ABSTRACT SHAPE SYSTEM ----------------

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, s):
        self.s = s

    def area(self):
        return self.s * self.s


class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r


# ---------------- PAYMENT SYSTEM ----------------

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self):
        pass


class CreditCard(PaymentMethod):
    def pay(self):
        return "Paid using Credit Card"


class UPI(PaymentMethod):
    def pay(self):
        return "Paid using UPI"


# ---------------- TRAFFIC SYSTEM ----------------

class Vehicle(ABC):
    @abstractmethod
    def speed(self):
        pass


class Car(Vehicle):
    def speed(self):
        return "Car speed: 120 km/h"


class Bike(Vehicle):
    def speed(self):
        return "Bike speed: 80 km/h"


# ---------------- MAIN ----------------

print("=== Grade System ===")
g = GradeSystem()
g.update_grade(70)
g.update_grade(60)
print(g.get_grade())

print("\n=== Time Tracker ===")
t = TimeTracker()
print(t.log_access())
print(t.log_access())

print("\n=== Shapes ===")
c = Circle(5)
print("Circle Area:", c.area())

print("\n=== Payment ===")
p = UPI()
print(p.pay())

print("\n=== Traffic ===")
v = Car()
print(v.speed())