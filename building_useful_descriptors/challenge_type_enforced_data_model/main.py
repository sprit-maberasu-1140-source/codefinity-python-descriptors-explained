# Base validator descriptor
class Validator:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self._name)

    def __set__(self, obj, value):
        self.validate(self._name, value)
        obj.__dict__[self._name] = value

    def validate(self, name, value):
        raise NotImplementedError("Subclasses must implement validate()")

# Positive number validator
class PositiveFloat(Validator):
    def validate(self, name, value):
        if not isinstance(value, (float, int)) or value <= 0:
            raise ValueError(f"{name} must be a positive number, got {value!r}")

# Non-empty string validator
class NonEmptyString(Validator):
    def validate(self, name, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{name} must be a non-empty string, got {value!r}")

class Trade:
    ticker = NonEmptyString()
    quantity = PositiveFloat()
    price = PositiveFloat()

    def __init__(self, ticker, quantity, price):
        self.ticker = ticker
        self.quantity = quantity
        self.price = price

class Account:
    account_id = NonEmptyString()
    balance = PositiveFloat()

    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

trade = Trade(ticker="AAPL", quantity=50.0, price=189.50)
account = Account(account_id="ACC-001", balance=10000.0)

print(trade.ticker, trade.quantity, account.account_id, account.balance)