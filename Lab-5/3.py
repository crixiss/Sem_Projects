class BankAccount:
    def __init__(self, holder, number, balance):
        self.holder = holder
        self.number = number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Not enough balance")

    def show_balance(self):
        print("Current Balance:", self.balance)

acc1 = BankAccount("Saksham", "99999", 10001)
acc1.deposit(5000)
print("after deposit")
acc1.show_balance()
acc1.withdraw(3000)
print("after withdraw")
acc1.show_balance()
