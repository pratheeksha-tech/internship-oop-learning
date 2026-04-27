# bank_system.py

class BankAccount:
    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self.balance = balance

    def display_account(self):
        print("Account Holder:", self.holder_name)
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):
    def __init__(self, holder_name, balance, interest_rate):
        super().__init__(holder_name, balance)
        self.interest_rate = interest_rate

    def show_details(self):
        self.display_account()
        print("Interest Rate:", self.interest_rate, "%")


# Example usage
acc = SavingsAccount("Lakshmi", 5000, 5)
acc.show_details()