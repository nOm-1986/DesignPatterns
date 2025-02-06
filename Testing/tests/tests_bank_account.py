import unittest
# from src.ba
from src.bank_account import BankAccount

class BankAccountTests(unittest.TestCase):
    # setUp se ejecuta siempre antes de hacer una prueba, es como un constructor ak podemos crear la instancia
    def setUp(self):
        self.account = BankAccount(1000)
    
    # tearDown se ejecuta al final

    def test_deposit(self):
        #account = BankAccount(1000)
        assert self.account.deposit(200) == 1200

    def test_withdraw(self):
        #account = BankAccount(1000)
        assert self.account.withdraw(400) == 600

    def test_get_balance(self):
        #account = BankAccount(2000)
        assert self.account.get_balance() == 1000

    def test_transfer(self):
        target = BankAccount(500)
        self.account.transfer(900, target)
        #Balance cuenta transmisora
        self.assertEqual(self.account.get_balance(), 100)
        #Balance cuenta receptora
        self.assertEqual(target.get_balance(), 1400)

    def test_insufficient_funds_transfer(self):
        target = BankAccount(balance=500)
        with self.assertRaises(ValueError) as context:
            self.account.transfer(2000, target)
        self.assertEqual(str(context.exception), "You do not have enough money")