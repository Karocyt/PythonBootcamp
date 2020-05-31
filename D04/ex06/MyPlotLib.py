import pandas as pd
from FileLoader import FileLoader


class MyPlotLib():
    @staticmethod
    def histogram(data, features):
        """plots one histogram for each numerical feature in the list"""
        pass

    @staticmethod
    def density(data, features):
        """plots the density curve of each numerical feature in the list"""
        pass

    @staticmethod
    def pair_plot(data, features):
        """plots a matrix of subplots (also called scatter plot matrix). On each subplot shows a scatter plot of one numerical variable against another one. The main diagonal of this
matrix shows simple histograms."""
        pass

    @staticmethod
    def box_plot(data, features):
        """displays a box plot for each numerical variable in the dataset"""
        pass


if __name__ == "__main__":
    loader = FileLoader()
    df = loader.load("../assets/athlete_events.csv")
    print(howManyMedals(df, 'Kjetil Andr Aamodt'))
