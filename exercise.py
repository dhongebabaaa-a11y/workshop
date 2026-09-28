class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Error: Insufficient balance!")
        else:
            self.balance -= amount

    def check_balance(self):
        print(self.balance)


acc = BankAccount()
acc.deposit(100)
acc.check_balance()

acc.withdraw(50)
acc.check_balance()