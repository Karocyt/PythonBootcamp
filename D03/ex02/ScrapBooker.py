import numpy as np


class ScrapBooker():
    def crop(self, arr, dimensions, position=(0, 0)):
        """crops the image as a rectangle with the given dimensions
(meaning, the new height and width for the image), whose top left corner
is given by the position argument. The position should be (0,0) by default.
You have to consider it an error (and handle said error)
if dimensions is larger than the current image size."""
        y, x = arr.shape
        startx, starty = position
        return arr.copy()[startx:startx+dimensions[0], starty:starty+dimensions[1]]

    def thin(self, arr, n, axis):
        """deletes every n-th pixel row along the specified axis
(0 vertical, 1 horizontal), example below."""
        axis = (axis + 1) % 2
        to_del = list(range(0, arr.shape[axis], n))
        return np.delete(arr, to_del, axis)

    def juxtapose(self, arr, n, axis):
        """juxtaposes n copies of the image along the specified axis
(0 vertical, 1 horizontal)."""
        return np.concatenate([arr for i in range(n)], axis)

    def mosaic(self, arr, dimensions):
        """makes a grid with multiple copies of the array. The dimensions
argument specifies the dimensions (meaning the height and width) of the
grid (e.g. 2x3)."""
        ret = self.juxtapose(arr, dimensions[0] // arr.shape[0] + 1, 1)
        ret = self.juxtapose(ret, dimensions[1] // arr.shape[1] + 1, 0)
        return ret[:dimensions[0], :dimensions[1]]


def test_thin():
    sb = ScrapBooker()
    a1 = np.array([[1.0, 3.0],
                   [2.0, 4.0]])
    a2 = sb.thin(np.array([[1.0, 2.0, 3.0, 4.0],
                           [2.0, 3.0, 4.0, 5.0]]),
                 2, 0)
    print("a1", a1.shape, a1)
    print("a2", a2.shape, a2)
    assert np.array_equal(a1, a2)


def test_crop():
    sb = ScrapBooker()
    a1 = np.array([[22.0], [32.0]])
    a2 = sb.crop(np.array([[11.0, 12.0, 13.0, 14.0],
                           [21.0, 22.0, 23.0, 24.0],
                           [31.0, 32.0, 33.0, 34.0]]),
                 (2, 1), (1, 1))
    print("a1", a1.shape, a1)
    print("a2", a2.shape, a2)
    assert np.array_equal(a1, a2)

    a1 = np.array([[2.0], [3.0]])
    a2 = sb.crop(np.array([[1.0, 2.0, 3.0, 4.0],
                           [2.0, 3.0, 4.0, 5.0]]),
                 (2, 1), (0, 1))
    print()
    print("a1", a1.shape, a1)
    print("a2", a2.shape, a2)
    assert np.array_equal(a1, a2)


def test_juxtapose():
    sb = ScrapBooker()
    a1 = np.array([[1.0, 2.0, 3.0, 4.0],
                   [2.0, 3.0, 4.0, 5.0],
                   [1.0, 2.0, 3.0, 4.0],
                   [2.0, 3.0, 4.0, 5.0],
                   [1.0, 2.0, 3.0, 4.0],
                   [2.0, 3.0, 4.0, 5.0]
                   ])
    a2 = sb.juxtapose(np.array([[1.0, 2.0, 3.0, 4.0],
                                [2.0, 3.0, 4.0, 5.0]
                                ]), 3, 0)
    print("a1", a1.shape, a1)
    print("a2", a2.shape, a2)
    assert np.array_equal(a1, a2)


def test_mosaic():
    sb = ScrapBooker()
    a1 = np.array([[1.0, 2.0, 3.0, 4.0],
                   [2.0, 3.0, 4.0, 5.0],
                   [1.0, 2.0, 3.0, 4.0],
                   [2.0, 3.0, 4.0, 5.0]
                   ])
    a2 = sb.mosaic(np.array([[1.0, 2.0, 3.0, 4.0],
                             [2.0, 3.0, 4.0, 5.0]]),
                   (4, 4))
    print("a1", a1.shape, a1)
    print("a2", a2.shape, a2)
    assert np.array_equal(a1, a2)

    sb = ScrapBooker()
    a1 = np.array([[1.0, 2.0, 3.0, 4.0, 1.0],
                   [2.0, 3.0, 4.0, 5.0, 2.0],
                   [1.0, 2.0, 3.0, 4.0, 1.0],
                   [2.0, 3.0, 4.0, 5.0, 2.0]
                   ])
    a2 = sb.mosaic(np.array([[1.0, 2.0, 3.0, 4.0],
                             [2.0, 3.0, 4.0, 5.0]]),
                   (4, 5))
    print("a1", a1.shape, a1)
    print("a2", a2.shape, a2)
    assert np.array_equal(a1, a2)
