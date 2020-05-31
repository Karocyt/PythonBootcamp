import matplotlib.image as mpimg
import matplotlib.pyplot as plt


class ImageProcessor():

    def load(self, path):
        """opens the .png file specified by the path argument
and returns an array with the RGB values of the image pixels."""
        arr = mpimg.imread(path)
        print(f"Picture of {arr.shape[0]}x{arr.shape[1]} imported")
        return arr

    def display(self, arr):
        """takes a NumPy array and displays the corresponding RGB image."""
        plt.imshow(arr)
        plt.show()


if __name__ == "__main__":
    imp = ImageProcessor()
    arr = imp.load("../assets/logo_v4_noir.png")
    print(arr)
    imp.display(arr)

    plt.plot([1, 2, 3],[4, 3, 4])
    plt.show()
