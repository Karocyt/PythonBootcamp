import pandas as pd
from FileLoader import FileLoader


def youngestFellah(data, val):
    print("1", data.head())
    dataY = data[data.Year == val]
    print("2", dataY.head())
    print("3", data.head())
    return {
        'M': dataY[dataY.Sex == 'M'].Age.min(),
        'F': dataY[dataY.Sex == 'F'].Age.min()
    }


if __name__ == "__main__":
    loader = FileLoader()
    df = loader.load("../assets/athlete_events.csv")
    print(youngestFellah(df, 2004))
