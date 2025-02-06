class BankAccount:
    def __init__(self, balance: int = 0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
        return self.balance
    
    def get_balance(self):
        return self.balance
    
    def transfer(self,amount: int, target):
        if amount > 0 and self.balance > amount:
            target.deposit(amount)
            self.balance -= amount
            return self.balance
        else:
            raise ValueError('You do not have enough money')
        