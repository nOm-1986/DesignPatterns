import unittest, os
# from src.ba
from src.bank_account import BankAccount

class BankAccountTests(unittest.TestCase):
    # setUp se ejecuta siempre antes de hacer una prueba, es como un constructor ak podemos crear la instancia
    def setUp(self):
        self.account = BankAccount(1000, log_file="transaction_log.txt")
    
    # tearDown se ejecuta al final
    def tearDown(self):
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def test_deposit(self):
        #account = BankAccount(1000)
        #assert self.account.deposit(200) == 1200
        self.assertEqual(self.account.deposit(200), 1200, "Deposit balance is not equal !!!")

    def test_withdraw(self):
        #account = BankAccount(1000)
        #assert self.account.withdraw(400) == 600
        self.assertEqual(self.account.withdraw(400), 600, "Withdraw balance is not equal !!!")

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

    def test_transaction_log(self):
        assert self.account.deposit(500)
        #assert os.path.exists(self.account.log_file)
        self.assertTrue(self.account.log_file)
    
    def test_count_transactions(self):
        assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(100)
        assert self._count_lines(self.account.log_file) == 2

    def test_deposit_varios_ammounts(self):
        test_cases = [
            {"amount": 100, "expected": 1100},
            {"amount": 3000, "expected": 4000},
            {"amount": 2400, "expected": 3400},
        ]
        for case in test_cases:
            with self.subTest(case=case):
                self.account = BankAccount(balance=1000, log_file="transaction.txt")
                new_balance = self.account.deposit(case["amount"])
                self.assertEqual(new_balance, case["expected"])

    def _count_lines(self, filename):
        with open(filename, 'r') as f:
            return len(f.readlines())