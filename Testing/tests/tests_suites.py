import unittest
from tests_bank_account import BankAccountTests


def back_account_suite():
    #definimos la suite
    suite = unittest.TestSuite()
    #Agregamos los test o una clase de tests
    # Lo que estamos diciendo es, de la clase BankAccountTests ejectue test_deposit
    suite.addTest(BankAccountTests('test_deposit'))
    suite.addTest(BankAccountTests('test_withdraw'))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2, durations=True,)
    runner.run(back_account_suite())