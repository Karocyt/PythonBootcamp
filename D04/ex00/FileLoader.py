import pandas as pd


class FileLoader():
    @staticmethod
    def load(path, header=True):
        """takes as an argument the file path of the dataset to load, displays a message specifying the
    dimensions of the dataset (e.g. 340 x 500) and returns the dataset loaded as a pandas.DataFrame."""
        header = ([0] if header else None)
        ret = pd.read_csv(path, header=header)
        print(f"Loading dataset of dims {ret.shape[0]} x {ret.shape[1]}")
        return ret

    @staticmethod
    def display(df, n):
        """takes a pandas.DataFrame and an integer as arguments, displays the first n rows of the
    dataset if n is positive, or the last n rows if n is negative."""
        if n > 0:
            print(df.head(n))
        else:
            print(df.tail(-n))


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load("../assets/athlete_events.csv")
    loader.display(data, 12)
    loader.display(data, -12)
