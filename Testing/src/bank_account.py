class BankAccount:
    def __init__(self, balance: int = 0, log_file:str=None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction('Cuenta creada')

    def _log_transaction(self, message: str):
        if self.log_file:
            with open(self.log_file, 'a') as f:
                f.write(f"{message}\n")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._log_transaction(f"Deposited {amount}. New balance {self.balance}")
        return self.balance

    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
            self._log_transaction(f"Withdrew {amount}. New balance {self.balance}")
        return self.balance
    
    def get_balance(self):
        self._log_transaction(f"Balance checked")
        return self.balance
    
    def transfer(self,amount: int, target):
        if amount > 0 and self.balance > amount:
            target.deposit(amount)
            self.balance -= amount
            return self.balance
        else:
            self._log_transaction(f"You can not perfomece this action. Balance {self.balance}")
            raise ValueError('You do not have enough money')
        