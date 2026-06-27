# Implementing a simplified version of property
class SimpleProperty:
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)

    def setter(self, fset):
        return SimpleProperty(self.fget, fset, self.fdel)

    def deleter(self, fdel):
        return SimpleProperty(self.fget, self.fset, fdel)

class Portfolio:
    def __init__(self, portfolio_id, value):
        self.portfolio_id = portfolio_id
        self._value = value

    @SimpleProperty
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value < 0:
            raise ValueError(f"Portfolio value cannot be negative, got {new_value!r}")
        self._value = new_value

    @value.deleter
    def value(self):
        self._value = 0.0

portfolio = Portfolio(portfolio_id="PF-001", value=50000.0)

initial_value = portfolio.value
portfolio.value = 75000.0
updated_value = portfolio.value

print(initial_value, updated_value)