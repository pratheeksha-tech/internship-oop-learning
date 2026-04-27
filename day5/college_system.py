# college_system.py

class Academic:
    def __init__(self, marks):
        self.marks = marks

    def show_academic(self):
        print("Academic Marks:", self.marks)


class Sports:
    def __init__(self, sport_name):
        self.sport_name = sport_name

    def show_sports(self):
        print("Sports:", self.sport_name)


class Student(Academic, Sports):
    def __init__(self, name, marks, sport_name):
        Academic.__init__(self, marks)
        Sports.__init__(self, sport_name)
        self.name = name

    def show_profile(self):
        print("Student Name:", self.name)
        self.show_academic()
        self.show_sports()


# Example usage
s = Student("Pratheeksha", 85, "Cricket")
s.show_profile()