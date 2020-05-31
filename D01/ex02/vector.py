#! /usr/bin/env python3

class Vector:
    """Class Vector contains a 1D vector of floats of any size"""

    def __init__(self, param=0):
        """ Initialize a new Vector depending on parameter"""
        if type(param) is int:
            self.values = [float(i) for i in range(0, param)]
        elif type(param) is list and all(isinstance(x, float) for x in param):
            self.values = [float(i) for i in param]
        elif type(param) is range:
            self.values = [float(i) for i in param]
        elif type(param) is tuple and (len(param) == 2 and
                                       all(isinstance(x, int) for x in param)):
            self.values = [float(i) for i in range(param[0], param[1])]
        else:
            raise ValueError("A Vector can only be initialized "
                             "from a list[float], an int or a range."
                             f" (param was of type {type(param)})")

    @property
    def size(self) -> int:
        """ Returns the len of the Vector as a dynamic attribute"""
        return len(self.values)

    def __str__(self):
        """ Returns a formatted string of the Vector """
        return f"(Vector {self.values})"

    def __add__(self, val):
        if type(val) is Vector:
            if self.size != val.size:
                raise ValueError("Vector are of different dimentionality")
            return Vector([(self.values[i] + val.values[i])
                           for i in range(0, self.size)])
        return NotImplemented

    def __radd__(self, val):
        return self + val

    def __sub__(self, val):
        if type(val) is Vector:
            if self.size != val.size:
                raise ValueError("Vector are of different dimentionality")
            return Vector([(self.values[i] - val.values[i])
                           for i in range(0, self.size)])
        return NotImplemented

    def __neg__(self):
        return Vector([-i for i in self.values])

    def __rsub__(self, val):
        return val + (-self)

    def __mul__(self, val):
        if type(val) is Vector:
            if self.size != val.size:
                raise ValueError("Vector are of different dimentionality")
            return Vector([(self.values[i] * val.values)
                           for i in range(0, self.size)])
        if type(val) is int or type(val) is float:
            return Vector([self.values[i] * float(val)
                           for i in range(0, self.size)])
        return NotImplemented

    def __rmul__(self, val):
        return self * val

    def __truediv__(self, val):
        if type(val) is Vector:
            if self.size != val.size:
                raise ValueError("Vector are of different dimentionality")
            return Vector([self.values[i] / val.values[i]
                           for i in range(0, self.size)])
        if isinstance(val, (int, float)):
            return Vector([self.values[i] / float(val)
                           for i in range(0, self.size)])
        return NotImplemented

    def __rtruediv__(self, val):
        return NotImplemented

    def __eq__(self, val):
        if type(val) is Vector:
            return self.values == val.values
        if type(val) is int or type(val) is float:
            if self.size == 1:
                return val == self.values[1]
        return False

    def __repr__(self):
        return self.values.__repr__()

    def __iter__(self):
        self.n = -1
        return self

    def __next__(self):
        if self.n < self.size - 1:
            self.n += 1
            return self.values[self.n]
        else:
            raise StopIteration
