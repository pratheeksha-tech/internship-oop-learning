# multiple_inheritance.py

class Father:
    def __init__(self, father_name, surname):
        self.father_name = father_name
        self.surname = surname

    def show_father(self):
        print("Father Name:", self.father_name)
        print("Surname:", self.surname)


class Mother:
    def __init__(self, mother_name):
        self.mother_name = mother_name

    def show_mother(self):
        print("Mother Name:", self.mother_name)


class Child(Father, Mother):
    def __init__(self, father_name, mother_name, surname):
        Father.__init__(self, father_name, surname)
        Mother.__init__(self, mother_name)

    def show_details(self):
        print("---- Child Full Details ----")
        self.show_father()
        self.show_mother()


# Example usage
c1 = Child("Ramesh", "Lakshmi", "Shetty")
c1.show_details()