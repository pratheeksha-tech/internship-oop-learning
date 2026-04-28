
# ---------------- DELIVERY BOT ----------------

class DeliveryBot:
    def status(self):
        return "Standard Delivery"


class FastDeliveryBot(DeliveryBot):
    def status(self):   # method overriding
        return "Fast Delivery in Progress"


# ---------------- SPACE ROBOT ----------------

class SpaceRobot:
    def communicate(self):
        return "Normal Communication"


class ExplorationRobot(SpaceRobot):
    def communicate(self):  # overriding
        return "Exploration Signal Active"


# ---------------- FANTASY CREATURE ----------------

class Creature:
    def battle_cry(self):
        return "Generic Cry"


class Dragon(Creature):
    def battle_cry(self):
        return "?? Dragon Roars Fiercely!"


# ---------------- SMART APPLIANCE ----------------

class Appliance:
    def status(self):
        return "Offline"


class SmartAppliance(Appliance):
    def status(self):
        return "Connected to Smart Network"


# ---------------- ATM SYSTEM (ENCAPSULATION) ----------------

class ATM:
    def __init__(self):
        self.__balance = 1000  # private variable

    def show_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance


# ---------------- EXAM SYSTEM ----------------

class Exam:
    def __init__(self):
        self.__score = 0

    def update_score(self, marks):
        if marks > self.__score:
            self.__score = marks

    def get_score(self):
        return self.__score


# ---------------- LOYALTY SYSTEM ----------------

class Loyalty:
    def __init__(self):
        self.points = 0

    def add_points(self, p):
        if p > 0:
            self.points += p


# ---------------- INVENTORY SYSTEM ----------------

class Inventory:
    def __init__(self):
        self.stock = 10

    def sell(self, qty):
        if qty <= self.stock:
            self.stock -= qty
            return "Sold"
        return "Not Enough Stock"


# ---------------- SAVINGS ACCOUNT ----------------

class Savings:
    def __init__(self):
        self._balance = 5000  # protected

    def add_interest(self):
        self._balance += self._balance * 0.05
        return self._balance


# ---------------- MAIN ----------------

print("=== Delivery Bot ===")
d = FastDeliveryBot()
print(d.status())

print("\n=== Space Robot ===")
s = ExplorationRobot()
print(s.communicate())

print("\n=== Dragon ===")
dr = Dragon()
print(dr.battle_cry())

print("\n=== ATM ===")
atm = ATM()
print("Balance:", atm.show_balance())
print("After Deposit:", atm.deposit(500))

print("\n=== Exam System ===")
e = Exam()
e.update_score(70)
e.update_score(60)
print("Final Score:", e.get_score())

print("\n=== Inventory ===")
inv = Inventory()
print(inv.sell(3))
print("Remaining Stock:", inv.stock)

print("\n=== Savings Account ===")
acc = Savings()
print("After Interest:", acc.add_interest())