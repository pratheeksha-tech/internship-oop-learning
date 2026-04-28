
# ---------------- HYBRID WORKER ----------------

class Worker:
    def work(self):
        return "Working..."


class Coder(Worker):
    def code(self):
        return "Writing Code"


class Designer(Worker):
    def design(self):
        return "Creating Design"


class HybridWorker(Coder, Designer):
    def profile(self):
        return self.work() + " | " + self.code() + " | " + self.design()


# ---------------- DRONE SYSTEM ----------------

class Drone:
    def fly(self):
        return "Drone Flying"


class Camera:
    def capture(self):
        return "Photo Captured"


class DroneSimulator(Drone, Camera):
    def status(self):
        return self.fly() + " + " + self.capture()


# ---------------- EBOOK READER ----------------

class Battery:
    def battery_status(self):
        return "Battery OK"


class Reader(Battery):
    def read(self):
        return "Reading eBook"


# ---------------- SMART ASSISTANT ----------------

class Speaker:
    def speak(self):
        return "Speaking Message"


class Scheduler:
    def schedule(self):
        return "Task Scheduled"


class SmartAssistant(Speaker, Scheduler):
    def assist(self):
        return self.speak() + " | " + self.schedule()


# ---------------- SALARY SYSTEM ----------------

class Employee:
    def salary(self, base, bonus):
        return base + bonus


# ---------------- LIBRARY SYSTEM ----------------

class Library:
    def issue(self, book, user, date):
        return f"{book} issued to {user} on {date}"


# ---------------- ONLINE STORE ----------------

class Product:
    def price(self, cost, discount):
        return cost - discount


# ---------------- TRAVEL SYSTEM ----------------

class Flight:
    def summary(self, source, dest):
        return f"Flight: {source} -> {dest}"


# ---------------- MAIN ----------------

print("=== Hybrid Worker ===")
h = HybridWorker()
print(h.profile())

print("\n=== Drone System ===")
d = DroneSimulator()
print(d.status())

print("\n=== Smart Assistant ===")
sa = SmartAssistant()
print(sa.assist())

print("\n=== Salary System ===")
e = Employee()
print("Total Salary:", e.salary(50000, 5000))

print("\n=== Library System ===")
lib = Library()
print(lib.issue("Python Book", "Rahul", "13-04-2026"))

print("\n=== Online Store ===")
p = Product()
print("Final Price:", p.price(1000, 200))

print("\n=== Travel System ===")
f = Flight()
print(f.summary("Bangalore", "Delhi"))