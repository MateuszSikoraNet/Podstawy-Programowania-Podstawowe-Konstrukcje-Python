class InvalidAmountError(ValueError):
    # No extra code is needed here.
    pass


class InsufficientFundsError(ValueError):
    # No extra code is needed here.
    pass


class BankAccount:
    def __init__(self, balance=0):
        # Save the balance in the account.
        pass

    def get_balance(self):
        # Return the current balance.
        pass

    def deposit(self, amount):
        # Raise InvalidAmountError if amount is not positive.

        # Add amount to the balance.
        pass

    def withdraw(self, amount):
        # Raise InvalidAmountError if amount is not positive.

        # Raise InsufficientFundsError if amount is greater than the balance.

        # Subtract amount from the balance.
        pass
