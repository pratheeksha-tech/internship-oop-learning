# inheritance_demo.py

class Father:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def display(self):
        print("Father Name:", self.name)
        print("Surname:", self.surname)


class Son(Father):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def show_identity(self):
        print("Son inherits family details:")
        self.display()


# Example usage
son1 = Son("Ramesh", "Shetty")
son1.show_identity()