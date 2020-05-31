import pandas as pd
from FileLoader import FileLoader


class SpatioTemporalData():

    def __init__(self, data):
        super().__init__()
        self.df = data.loc[:, ['Year', 'City']].drop_duplicates()
        print(self.df.head())

    def when(self, location):
        return list(self.df[self.df.City == location]['Year'])

    def where(self, date):
        return list(self.df[self.df.Year == date]['City'])


def test():
    loader = FileLoader()
    df = loader.load("../assets/athlete_events.csv")

    sp = SpatioTemporalData(df)
    assert sp.where(1896) == ['Athina']
    assert sp.where(2016) == ['Rio de Janeiro']
    assert sp.when('Athina') == [2004, 1906, 1896]
    assert sp.when('Paris') == [1900, 1924]
