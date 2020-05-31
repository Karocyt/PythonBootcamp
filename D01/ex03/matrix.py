#! /usr/bin/env python3
import importlib
import sys

sys.path.append('../ex02')


vector = importlib.import_module("vector")


class Matrix:
    """Class Matrix contains a Matrix of floats of any shape"""

    def __init__(self, param=[[0.0]], size=False):
        """ Initialize a new Matrix depending on parameter"""

        def get_shape(self) -> tuple:
            """ Returns the len of the Matrix as a dynamic attribute"""
            curr = self.data
            sizes = []
            while type(curr) is list and not all(isinstance(x, float)
                                                 for x in curr):
                sizes += len(curr),
                curr = curr[0]
            if type(curr) is list and all(isinstance(x, float) for x in curr):
                sizes += [len(curr)]
                return tuple(s for s in sizes)
            raise ValueError(
                "This Matrix does not contains only floats ({curr[0]})")

        if type(param) is list and all(isinstance(x, list) for x in param):
            self.data = param
            if size and size != self.shape:
                raise ValueError("Incompatible shape and content")
        elif type(param) is tuple and (len(param) == 2 and
                                       param[0] > 0 and param[1] > 0):
            self.data = []
            for i in range(param[0]):
                self.data += [[0.0 for j in range(param[1])]]
        elif type(param) is vector.Vector:
            self.data = [[nb] for nb in param.values]  # [param.values]#
        else:
            raise ValueError("A Matrix can only be initialized "
                             "from a list[float], an int or a range."
                             f" (param was of type {type(param)})")
        self.shape = get_shape(self)

    def __repr__(self):
        return self.data.__repr__()

    def __str__(self):
        """ Returns a formatted string of the Matrix """
        mat = ",\n    ".join(str(x) for x in self.data)
        return f"Matrix([\n    {mat}\n    ])"

    def transform(fn, data):
        """ Apply fn on each float of the matrix"""
        if type(data) is list and all(isinstance(x, list) for x in data):
            return [Matrix.transform(fn, elem) for elem in data]
        if type(data) is list and all(isinstance(x, float) for x in data):
            return [fn(elem) for elem in data]
        raise ValueError(
            "This Matrix does not contains only floats ({curr[0]})")

    def __neg__(self):
        """Come on, you know."""
        return Matrix(Matrix.transform(lambda x: -x, self.data))

    def __add__(self, val):
        if type(val) is Matrix:
            if self.shape != val.shape:
                raise ValueError("Matrices are of different dimentionality")
            return Matrix([[self.data[i][j] + val.data[i][j]
                            for j in range(0, len(self.data[i]))]
                           for i in range(0, len(self.data))])
        return NotImplemented

    def __radd__(self, val):
        return self + val

    def __sub__(self, val):
        if type(val) is Matrix:
            if self.shape != val.shape:
                raise ValueError("Matrices are of different dimentionality")
            return Matrix([[self.data[i][j] + val.data[i][j]
                            for j in range(0, len(self.data[i]))]
                           for i in range(0, len(self.data))])
        return NotImplemented

    def __rsub__(self, val):
        return NotImplemented

    def __mul__(self, val):
        if type(val) is vector.Vector:
            val = Matrix(val)
        if type(val) is Matrix:
            print(self.shape, val.shape)
            if self.shape[1] == val.shape[0]:
                ret = Matrix((self.shape[0], val.shape[1]))
                for i in range(self.shape[0]):
                    for j in range(val.shape[1]):
                        ret.data[i][j] = sum(
                            self.data[i][k] * val.data[k][j]
                            for k in range(val.shape[0]))
                return ret

            raise ValueError("Matrices are of incompatible dimentionality")
        if type(val) is int:
            return Matrix([self.data[i] * float(val)
                           for i in range(0, self.shape)])
        return NotImplemented

    def __rmul__(self, val):
        if type(val) is vector.Vector:
            return Matrix(val) * self
        return NotImplemented

    def __truediv__(self, val):
        if type(val) is Matrix:
            print(self.shape, val.shape)
            if self.shape[1] == val.shape[0]:
                ret = Matrix((self.shape[0], val.shape[1]))
                for i in range(self.shape[0]):
                    for j in range(val.shape[1]):
                        ret.data[i][j] = sum(self.data[i][k] / val.data[k][j]
                                             if val.data[k][j] != 0.0
                                             else float('NaN')
                                             for k in range(val.shape[0]))
                return ret

            raise ValueError("Matrices are of incompatible dimentionality")
        if type(val) is int:
            return Matrix([self.data[i] * float(val)
                           for i in range(0, self.shape)])
        return NotImplemented

    def __rtruediv__(self, val):
        return NotImplemented

    def __eq__(self, b):
        def list_compare(a, b):
            if type(a) != type(b):
                return False
            if type(a) != list:
                return a == b
            if len(a) != len(b):
                return False
            for a_, b_ in zip(a, b):
                if not list_compare(a_, b_):
                    return False
            return True
        if type(b) is Matrix:
            return list_compare(self.data, b.data)
        if type(b) is list:
            return list_compare(self.data, b)
        return False
