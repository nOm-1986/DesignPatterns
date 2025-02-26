class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_total_balance(self):
        return sum(map(lambda ac: ac.get_balance(), self.accounts))