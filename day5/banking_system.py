# banking_system.py

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


class SavingsAccount(Account):
    def interest(self):
        interest_amt = self.balance * 0.05
        print("Interest:", interest_amt)


class CurrentAccount(Account):
    def overdraft(self):
        print("Overdraft facility enabled")


# Example usage
acc1 = SavingsAccount("Ravi", 10000)
acc1.deposit(2000)
acc1.interest()
acc1.show_balance()