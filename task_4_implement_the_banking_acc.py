class Account:
    def __init__(self, title, balance=0):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = intrestRate

account = SavingsAccount("ashish", 500)
print(account.title)  
print(account.balance)  
print(account.interestRate)  

print(f"Account Holder : {account.title}\nAccount Balance : {account.balance}\nIntrestRate : {account.interestRate}")
