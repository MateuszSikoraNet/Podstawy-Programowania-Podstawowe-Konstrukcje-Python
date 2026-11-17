import unittest

from src.objects.error_handling import BankAccount, InsufficientFundsError, InvalidAmountError


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(100)

    def test_deposit_and_withdraw(self):
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 150)
        self.account.withdraw(30)
        self.assertEqual(self.account.get_balance(), 120)

    def test_non_positive_amount_raises_invalid_amount_error(self):
        with self.assertRaises(InvalidAmountError):
            self.account.deposit(0)
        with self.assertRaises(InvalidAmountError):
            self.account.withdraw(-1)

    def test_withdrawal_over_balance_raises_insufficient_funds_error(self):
        with self.assertRaises(InsufficientFundsError):
            self.account.withdraw(101)
        self.assertEqual(self.account.get_balance(), 100)

