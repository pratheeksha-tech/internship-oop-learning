# multilevel_inheritance.py

class Grandparent:
    def __init__(self, property_value):
        self.property_value = property_value

    def show_property(self):
        print("Grandparent Property:", self.property_value)


class Parent(Grandparent):
    def __init__(self, property_value, business):
        super().__init__(property_value)
        self.business = business

    def show_business(self):
        print("Parent Business:", self.business)


class Child(Parent):
    def __init__(self, property_value, business, education):
        super().__init__(property_value, business)
        self.education = education

    def show_all(self):
        print("---- Family Hierarchy ----")
        self.show_property()
        self.show_business()
        print("Child Education:", self.education)


# Example usage
c = Child("House & Land", "Textile Shop", "Engineering")
c.show_all()