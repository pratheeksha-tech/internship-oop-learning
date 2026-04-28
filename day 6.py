class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance  # Encapsulation (private data)

    # Getter
    def get_balance(self):
        return self.__balance

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    # Withdraw method
    def withdraw(self, amount):
        if amount <= self.__balance and amount > 0:
            self.__balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    def display(self):
        print(f"Account Holder: {self.name}")
        print(f"Current Balance: {self.__balance}")


# ---------------- MAIN PROGRAM ----------------

# Task 1: Create account (Account creation feature)
acc1 = Account("Pratheeksha", 1000)

# Task 2: Authentication (simple simulation)
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("\nLogin Successful!\n")

    # Task 3: Transactions
    acc1.display()

    acc1.deposit(500)
    acc1.withdraw(200)

    print("\nAfter Transactions:")
    acc1.display()

else:
    print("Invalid credentials. Access denied.")