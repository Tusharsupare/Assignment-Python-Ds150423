class Account:
    def __init__(self, title, balance=0):
        self.title = title
        self.balance = balance

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount

    def getAccountHolder(self):
        return self.title

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return self.interestRate * self.balance / 100

account = Account("Tushar Supare", 100000)
balance = account.getBalance()
print(f"Account Holder: {account.getAccountHolder()}")
print(f"Account Balance: ₹{balance}")

account.deposit(25000)
balance = account.getBalance()
print(f"Deposit Successful! Your Account Balance: ₹{balance}")

account.withdraw(20000)
balance = account.getBalance()
print(f"Withdraw Successful! Your Account Balance: ₹{balance}")

# Create an instance of SavingsAccount
savings_account = SavingsAccount("Tushar saving account", 100000, 5)
balance = savings_account.getBalance()
print(f"Account Holder: {savings_account.getAccountHolder()}")
print(f"Savings Account Balance: ₹{balance}")

interest_amount = savings_account.interestAmount()
print(f"Your Interest Amount: ₹{interest_amount}")