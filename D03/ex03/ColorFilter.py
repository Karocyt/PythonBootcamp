import numpy as np
from numba import jit

class ColorFilter():
    """Tool that can apply a variety of color filters on images"""

    @staticmethod
    @jit
    def invert(arr):
        """Takes a NumPy array of an image as an argument and returns an array with inverted
color.
Authorized functions: None
Authorized operator: -"""
        # if arr.shape[2] == 4:  # alpha_channel
        #     raise NotImplementedError("invert does not manages alpha channel")
        ret = 1.0 - arr
        return ret

    @staticmethod
    @jit
    def to_blue(arr):
        """Takes a NumPy array of an image as an argument and returns an array with a blue
filter.
Authorized functions: .zeros, .shape
Authorized operator: None"""
        ret = np.zeros(arr.shape)
        for i in range(ret.shape[0]):
            for j in range(ret.shape[1]):
                ret[i][j][2] = arr[i][j][2]
        return ret

    @staticmethod
    @jit
    def to_green(arr):
        """Takes a NumPy array of an image as an argument and returns an array with a green
filter.
Authorized functions: None
Authorized operator: *"""
        return arr * np.array([0.0, 1.0, 0.0])

    @staticmethod
    @jit(forceobj=True)
    def to_red(arr):
        """Takes a NumPy array of an image as an argument and returns an array with a red filter.
Authorized functions : to_green, to_blue
Authorized operator: -, +"""
        return arr - ColorFilter.to_blue(arr) - ColorFilter.to_green(arr)

    @staticmethod
    @jit
    def to_celluloid(arr, steps=5):
        """Takes a NumPy array of an image as an argument, and returns an array with a
celluloid shade filter. The celluloid filter must display at least four thresholds of shades. Be careful! You
are not asked to apply black contour on the object here (you will have to, but later. . . ), you only have to
work on the shades of your images.
Authorized functions: .arange, linspace"""
        grad = np.linspace(0.0, 1.0, steps)
        new = arr.copy()
        for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                for k in range(arr.shape[2]):
                    val = arr[i][j][k]
                    if val < grad[1] / 2:
                        val = 0
                    else:
                        for shade in grad[::-1]:
                            if val >= shade:
                                val = shade
                                break
                    new[i][j][k] = val

        return new

    @staticmethod
    @jit(forceobj=True)
    def to_grayscale(arr, f='w'):
        """Takes a NumPy array of an image as an argument and returns an array
in grayscale. The method takes another argument to select between two possible grayscale filters. Each
filter has specific authorized functions and operators.
– ‘mean’ or ‘m’ : Takes a NumPy array of an image as an argument and returns an array in grayscale
created from the mean of the RBG channels.
Authorized functions: .sum, .shape, reshape, broadcast_to, as_type
Authorized operator: /
– ‘weighted’ or ‘w’ : Takes a NumPy array of an image as an argument and returns an array in weighted
grayscale. This argument should be selected by default if not given.
The usual weighted grayscale is calculated as : 0.299 * R_channel + 0.587 * G_channel + 0.114 *
B_channel.
Authorized functions: .sum, .shape, .tile
Authorized operator: *"""

        shape = arr.shape
        ret = arr
        if f == 'm' or f == 'mean':
            ret = arr / 3
        elif f == 'w' or f == 'weighted':
            grad = np.tile([[0.299, 0.587, 0.114]], (shape[0], shape[1], 1))
            ret = arr * grad

        for x in range(ret.shape[0]):
            for y in range(ret.shape[1]):
                ret[x][y] = ret[x][y].sum()
        return ret


if __name__ == "__main__":
    from ImageProcessor import ImageProcessor
    imp = ImageProcessor()
    arr = imp.load("../assets/elon.png")
    print(arr)
    cf = ColorFilter()
    imp.display(cf.invert(arr))
    imp.display(cf.to_green(arr))
    imp.display(cf.to_red(arr))
    imp.display(cf.to_blue(arr))
    imp.display(cf.to_celluloid(arr))
    imp.display(cf.to_celluloid(arr, 4))
    imp.display(cf.to_celluloid(arr, 3))
    imp.display(cf.to_celluloid(arr, 2))
    imp.display(cf.to_grayscale(arr, 'weighted'))
    imp.display(cf.to_grayscale(arr, 'm'))
