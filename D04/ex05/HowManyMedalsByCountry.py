import pandas as pd
from FileLoader import FileLoader


def howManyMedalsByCountry(df, country):
    # Filtering Name
    df = df[df.Team == country].copy()

    # Remove empty Medals
    df = df[['Year', 'Medal']].dropna()

    # Rename Medals as str[0]
    df['Medal'] = df['Medal'].astype(str).str[0]

    # groupby Year
    df = df.groupby(['Year'])

    # Count Medals
    df = df.Medal.value_counts()

    # Unstack Medals column
    df = df.unstack('Medal', fill_value=0)
    print(df)

    return df.to_dict('index')


if __name__ == "__main__":
    loader = FileLoader()
    df = loader.load("../assets/athlete_events.csv")
    print(howManyMedalsByCountry(df, 'France'))
