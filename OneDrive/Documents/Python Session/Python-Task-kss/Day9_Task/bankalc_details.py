class BankAccount:

    def __init__(self, accno, balance):
        self.accno = accno
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def display(self):
        print("Account Number:", self.accno)
        print("Balance:", self.balance)

acc = BankAccount(1001, 5000)

acc.deposit(2000)
acc.withdraw(1000)
acc.display()
