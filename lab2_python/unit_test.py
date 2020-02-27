from lab2_python_class import BankAccount
import unittest

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(100)

    def test_account_deposit(self):
        test_balance = 150
        self.account.deposit(50)
        self.assertEqual(self.account.balance, test_balance)

    def test_account_withdrawtrue(self):
        test_balance = 50
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, test_balance)

    def test_account_withdrawfalse(self):
        test_balance = 100
        self.account.withdraw(500)
        self.assertEqual(self.account.balance, test_balance)

    def test_account_percents(self):
        test_balance=6300
        self.account.balance = 6000
        self.account.percents()
        self.assertEqual(self.account.balance,test_balance)

    def test_account_transfertrue(self):
        test_ba1 = 150
        ba2 = BankAccount(100)
        self.account.transfer_from(ba2, 50)
        self.assertEqual(self.account.balance, test_ba1)

    def test_account_transferfalse(self):
        test_ba1 = 100
        ba2 = BankAccount(100)
        self.account.transfer_from(ba2, 500)
        self.assertEqual(self.account.balance, test_ba1)
   
if __name__ == '__main__':
    unittest.main()