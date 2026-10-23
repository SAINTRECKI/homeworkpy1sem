class BankError(Exception):
    pass
class InvalidAmountError(BankError):
    pass
class InsufficientFundsError(BankError):
    pass
class AccountBlockedError(BankError):
    pass

def withdraw(balance, amount):
    if amount <= 0:
        raise InvalidAmountError()
    if amount > balance:
        raise InsufficientFundsError()
    return balance - amount