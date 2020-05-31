from NumPyCreator import NumPyCreator
npc = NumPyCreator()

import numpy as np

def test_from_list():
    assert np.array_equal(npc.from_list([[1,2,3],[6,3,4]]),
                          np.array([[1, 2, 3],
                                    [6, 3, 4]]))

def test_from_tuple():
    assert np.array_equal(npc.from_tuple(("a", "b", "c")),
                          np.array(['a', 'b', 'c']))

def test_from_iterable():
    assert np.array_equal(npc.from_iterable(range(5)),
                          np.array([0, 1, 2, 3, 4]))


def test_from_shape():
    shape=(3,5)
    assert np.array_equal(npc.from_shape(shape),
                          np.array([[0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0]]))


def test_random():
    shape=(3,5)
    assert npc.random(shape).shape == shape


def test_identity():
    assert np.array_equal(npc.identity(4),
                          np.array([[1., 0., 0., 0.],
                                    [0., 1., 0., 0.],
                                    [0., 0., 1., 0.],
                                    [0., 0., 0., 1.]]))