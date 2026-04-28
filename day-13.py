
# ---------------- BASE SYSTEM ----------------

class BaseSystem:
    def info(self):
        return "Base System Active"


# ---------------- SMART ECOSYSTEM (MULTI FEATURES) ----------------

class SmartEcoSystem(BaseSystem):
    def device_control(self):
        return "Device Control Enabled"

    def user_management(self):
        return "User Management Enabled"

    def analytics(self):
        return "Analytics Module Running"


# ---------------- EDUCATION PLATFORM ----------------

class EducationPlatform(BaseSystem):
    def __init__(self, name):
        self.name = name

    def student_module(self):
        return f"{self.name} - Student Module Active"

    def course_module(self):
        return f"{self.name} - Course Module Active"


# ---------------- TRANSPORT SYSTEM ----------------

class TransportBase:
    def rider(self):
        return "Rider Data"

    def driver(self):
        return "Driver Data"


class RideService(TransportBase):
    def trip_summary(self):
        return f"{self.rider()} + {self.driver()} => Trip Created"


# ---------------- E-COMMERCE SYSTEM ----------------

class ProductBase:
    def product_info(self):
        return "Product Base Info"


class Digital(ProductBase):
    def feature(self):
        return "Digital Product Features"


class Physical(ProductBase):
    def feature(self):
        return "Physical Product Features"


# ---------------- ORGANIZATION SYSTEM ----------------

class Organization:
    def company(self):
        return "Company Level"


class Department(Organization):
    def department(self):
        return "Department Level"


class Employee(Department):
    def employee(self):
        return "Employee Level"


# ---------------- MAIN EXECUTION ----------------

print("=== SMART ECOSYSTEM ===")
eco = SmartEcoSystem()
print(eco.info())
print(eco.device_control())

print("\n=== EDUCATION PLATFORM ===")
edu = EducationPlatform("LMS Platform")
print(edu.student_module())
print(edu.course_module())

print("\n=== TRANSPORT SYSTEM ===")
ride = RideService()
print(ride.trip_summary())

print("\n=== E-COMMERCE SYSTEM ===")
d = Digital()
p = Physical()
print(d.product_info(), "-", d.feature())
print(p.product_info(), "-", p.feature())

print("\n=== ORGANIZATION SYSTEM ===")
emp = Employee()
print(emp.company(), emp.department(), emp.employee())