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

    def test_default_balance_is_zero(self):
        self.assertEqual(BankAccount().get_balance(), 0)

    def test_smallest_valid_amounts_and_exact_balance(self):
        self.account.deposit(1)
        self.account.withdraw(1)
        self.account.withdraw(100)
        self.assertEqual(self.account.get_balance(), 0)

    def test_zero_withdrawal_raises_invalid_amount_error(self):
        with self.assertRaises(InvalidAmountError):
            self.account.withdraw(0)

    def test_failed_operations_do_not_change_the_balance(self):
        for operation, amount in ((self.account.deposit, -5), (self.account.withdraw, 0), (self.account.withdraw, 500)):
            with self.assertRaises(ValueError):
                operation(amount)
        self.assertEqual(self.account.get_balance(), 100)

    def test_custom_errors_are_caught_by_their_base_class(self):
        # except ValueError also catches every subclass of ValueError.
        self.assertTrue(issubclass(InvalidAmountError, ValueError))
        self.assertTrue(issubclass(InsufficientFundsError, ValueError))
        try:
            self.account.withdraw(1000)
        except ValueError as error:
            self.assertIsInstance(error, InsufficientFundsError)
        else:
            self.fail("withdraw(1000) should raise")
