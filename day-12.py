
# ---------------- SMART DEVICE CONTROL ----------------

class Device:
    def control(self):
        return "Device Controlled"


class SmartDevice(Device):
    def feature(self):
        return "Smart Features Enabled"


# ---------------- COLLEGE SYSTEM ----------------

class College:
    def role(self):
        return "College Entity"


class Admin(College):
    def academic(self):
        return "Academic Management"

class Staff(College):
    def operations(self):
        return "Operational Management"


# ---------------- RIDE BOOKING ----------------

class Rider:
    def rider_info(self):
        return "Rider Details"


class Driver:
    def driver_info(self):
        return "Driver Details"


class Ride(Rider, Driver):
    def trip(self):
        return self.rider_info() + " + " + self.driver_info()


# ---------------- E-COMMERCE SYSTEM ----------------

class Product:
    def info(self):
        return "Basic Product Info"


class DigitalProduct(Product):
    def digital(self):
        return "Digital Features"


class PhysicalProduct(Product):
    def physical(self):
        return "Physical Features"


# ---------------- ORGANIZATION SYSTEM ----------------

class Company:
    def company(self):
        return "Company Level"


class Department(Company):
    def dept(self):
        return "Department Level"


class Employee(Department):
    def emp(self):
        return "Employee Level"


# ---------------- ANIMAL SYSTEM ----------------

class Animal:
    def sound(self):
        return "Animal Sound"


class Dog(Animal):
    def sound(self):
        return "Dog Barks"


# ---------------- MAIN ----------------

print("=== Ride System ===")
r = Ride()
print(r.trip())

print("\n=== Organization ===")
e = Employee()
print(e.company(), e.dept(), e.emp())

print("\n=== Animal System ===")
d = Dog()
print(d.sound())

print("\n=== Smart Device ===")
sd = SmartDevice()
print(sd.control(), sd.feature())