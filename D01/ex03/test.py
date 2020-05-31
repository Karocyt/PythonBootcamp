#! /usr/bin/env python3

import importlib
from matrix import Matrix
import sys

sys.path.append('../ex02')


vector = importlib.import_module("vector")


def test_crea():  # basic creation
    assert Matrix()
    assert Matrix((1, 1)) == Matrix([[0.0]])
    assert Matrix([[1.02, 1.03]])


def test_crea_tuple():
    assert Matrix((1, 2))


def test_shape():
    assert Matrix([[1.02, 1.03]]).shape == tuple((1, 2))


def test_neg():
    assert -Matrix([[1.0, 0.0], [0.0, 1.0]]
                   ) == Matrix([[-1.0, 0.0], [0.0, -1.0]])


def test_git():
    I2 = Matrix([
        [1.0, 0.0],
        [0.0, 1.0]
    ])
    I2_neg = Matrix([
        [-1.0, 0.0],
        [0.0, -1.0]
    ])

    zero = Matrix([
        [0.0, 0.0],
        [0.0, 0.0]
    ])

    m1 = Matrix([
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0]
    ])

    m2 = Matrix([
        [7.0, -2.0],
        [-3.0, -5.0],
        [4.0, 1.0]
    ])

    m1_x_m2 = Matrix([
        [13.0,  -9.0],
        [37.0, -27.0]])

    m2_x_m1 = Matrix([
        [-1.0,   4.0,   9.0],
        [-23.0, -31.0, -39.0],
        [8.0,  13.0,  18.0]])

    assert -I2 == I2_neg, "Error in your __neg__ function"
    added = I2 + I2_neg
    assert added == zero, "Error in your __add__ function"
    mul = m1 * m2
    assert mul == m1_x_m2, "Error in your __mul__ function"
    mul = m2 * m1
    assert mul == m2_x_m1, "Error in your __mul__ function"


def test_mul():
    assert Matrix([[1.0, 0.0], [0.0, 1.0]]) * vector.Vector([1.0, 0.0])


def test_rmul():
    assert vector.Vector([1.0, 0.0]) * Matrix([[1.0, 0.0, 2.0]])


def test_div():
    assert Matrix([[1.0, 0.0], [0.0, 1.0]]) / Matrix([[1.0], [0.0]])


def test_rdiv():
    assert Matrix([[1.0], [0.0]]) / Matrix([[1.0, 0.0, 1.0]])


if __name__ == "__main__":
    print(Matrix([[1.0, 2.0], [3.0, 4.0]]))
