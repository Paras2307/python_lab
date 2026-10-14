# Base class
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


# Derived class 1
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        print("Savings Account Withdrawal")
        super().withdraw(amount)


# Derived class 2
class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        print("Current Account Withdrawal")
        super().withdraw(amount)


# Create objects
s1 = SavingsAccount("Rahul", 5000)
c1 = CurrentAccount("Amit", 10000)

# Savings account operations
s1.deposit(1000)
s1.withdraw(2000)
print("Savings Balance:", s1.get_balance())

# Current account operations
c1.deposit(2000)
c1.withdraw(3000)
print("Current Balance:", c1.get_balance())