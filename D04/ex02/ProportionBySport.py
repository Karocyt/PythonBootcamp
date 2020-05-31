import pandas as pd
from FileLoader import FileLoader


def proportionBysport(df, year, sport, gender):
    tot = df[(df.Year == year) & (df.Sex == gender)]
    # print("\ntot1", tot.shape, tot.head())
    players = tot[tot.Sport == sport]
    # print("\nplayers", players.shape, players.head())
    # print(len(players), "/", len(tot))
    players = players.drop_duplicates(subset="Name", keep='first')
    # print("\nplayers", players.shape, players.head())
    # print(len(players), "/", len(tot))
    tot = tot[(~(tot["Name"].isin(players)))].dropna()
    # print("\ntot2", tot.shape, tot)
    # print(len(players), "/", len(tot))
    return len(players)/(len(tot) + len(players))


if __name__ == "__main__":
    loader = FileLoader()
    df = loader.load("../assets/athlete_events.csv")
    # print(df.describe())
    print(proportionBysport(df, 2004, 'Tennis', 'F'))
