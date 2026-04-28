from abc import ABC, abstractmethod

# ---------------- TASK 1: ABSTRACTION ----------------

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Dog barks"


class Cat(Animal):
    def sound(self):
        return "Cat meows"


# ---------------- TASK 2: CLASS VARIABLES + CLASSMETHOD ----------------

class Student:
    school_name = "Global Tech School"
    student_count = 0

    def __init__(self, name):
        self.name = name
        Student.student_count += 1

    @classmethod
    def get_student_count(cls):
        return cls.student_count


# ---------------- TASK 3: STATIC METHOD ----------------

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b


# ---------------- DECORATOR (SECURITY SYSTEM) ----------------

def security_check(func):
    def wrapper(user):
        if user == "admin":
            return func(user)
        else:
            return "Access Denied"
    return wrapper


@security_check
def dashboard(user):
    return "Welcome to Security Dashboard"


# ---------------- MAIN PROGRAM ----------------

print("=== Animal Sound System ===")
dog = Dog()
cat = Cat()
print(dog.sound())
print(cat.sound())

print("\n=== Student System ===")
s1 = Student("Pratheeksha")
s2 = Student("Rahul")
print("Total Students:", Student.get_student_count())

print("\n=== Math Utility ===")
print("Addition:", MathUtils.add(10, 20))

print("\n=== Security Dashboard ===")
print(dashboard("admin"))
print(dashboard("user"))