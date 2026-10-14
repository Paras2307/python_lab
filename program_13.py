# Base class
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance or invalid amount!")

    def get_balance(self):
        return self.__balance


# Derived class: Savings Account
class SavingsAccount(BankAccount):
    def __init__(self, name, balance, interest):
        super().__init__(name, balance)
        self.interest = interest

    def calculate_interest(self):
        return self.get_balance() * self.interest / 100


# Derived class: Current Account
class CurrentAccount(BankAccount):
    def __init__(self, name, balance, overdraft):
        super().__init__(name, balance)
        self.overdraft = overdraft

    # Method overriding
    def withdraw(self, amount):
        if 0 < amount <= self.get_balance() + self.overdraft:
            super().withdraw(amount) if amount <= self.get_balance() else print(
                "Overdraft facility used:", amount - self.get_balance()
            )
            if amount > self.get_balance():
                remaining = self.get_balance() - amount
                self.deposit(remaining * -1) if remaining < 0 else None
        else:
            print("Overdraft limit exceeded!")


# Main program
savings = SavingsAccount("Rahul", 10000, 5)
current = CurrentAccount("Aman", 5000, 2000)

print("Savings Account")
savings.deposit(2000)
print("Balance:", savings.get_balance())
print("Interest:", savings.calculate_interest())

print("\nCurrent Account")
current.withdraw(6000)
print("Balance:", current.get_balance())

# Polymorphism
print("\nPolymorphism Example")
accounts = [savings, current]

for account in accounts:
    print(account.name, "Balance:", account.get_balance())