class Cell:

    _value: int

    def __init__(self, value:int = 0):
        self._value = value

    def __eq__(self, other):
        return self._value == other._value

    def __add__(self, other):
        if (self._value == 0) or (self == other):
            return (Cell(self._value + other._value), Cell(0))
        return (self, other)