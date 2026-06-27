# Implementing a validated bounded float descriptor
class BoundedFloat:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self._name)

    def __set__(self, obj, value):
        if not isinstance(value, (float, int)):
            raise TypeError(f"{self._name} must be a number, got {value!r}")
        if not (self.min_value <= value <= self.max_value):
            raise ValueError(
                f"{self._name} must be between {self.min_value} and {self.max_value}"
            )
        obj.__dict__[self._name] = value

class Position:
    quantity = BoundedFloat(min_value=0.0, max_value=10000.0)
    price = BoundedFloat(min_value=0.01, max_value=999999.99)

    def __init__(self, ticker, quantity, price):
        self.ticker = ticker
        self.quantity = quantity
        self.price = price

# Creating a Position instance
position = Position(ticker="AAPL", quantity=100.0, price=189.50)

qty = position.quantity
prc = position.price

print(qty, prc)