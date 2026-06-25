"""
Practice: Classes & Objects
"""
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount")

    def get_balance(self):
        return self.balance

if __name__ == "__main__":
    acc = BankAccount("Murali", 1000)
    acc.deposit(500)
    acc.withdraw(300)
    acc.withdraw(2000)
    print(f"Final balance: {acc.get_balance()}")
