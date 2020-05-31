import pandas as pd
from FileLoader import FileLoader
import seaborn as sns
import matplotlib.pyplot as plt

class Komparator():

    @staticmethod
    def compare_box_plots(categorical_var, numerical_var): 
        """displays a series of box plots to compare how
the distribution of the numerical variable changes if we only consider the subpopulation which belongs to
each category. There should be as many box plots as categories. For example, with Sex and Height, we
would compare the height distributions of men vs. women with two box plots."""

        sns.boxplot(x=categorical_var, y=numerical_var, palette="Set2")

        plt.show()

    @staticmethod
    def density(categorical_var, numerical_var): 
        """displays the density of the numerical variable. Each
subpopulation should be represented by a separate curve on the graph."""
        #print(categorical_var)
        cat_list = categorical_var.astype('category')
        for cat in cat_list:
            sns.kdeplot(numerical_var[categorical_var == cat], label=cat)#, categorical_var)

        plt.show()
    
    @staticmethod
    def compare_histograms(categorical_var, numerical_var): 
        """plots the numerical variable in a s"""
        pass

if __name__ == "__main__":
    loader = FileLoader()
    df = loader.load("../assets/athlete_events.csv").dropna()
    h = df[df.Sex=="M"]
    f = df[df.Sex=="F"]
    k = Komparator()
    k.compare_box_plots(df.Sex, df.Weight)
    k.density(df.Sex, df.Weight)
    k.compare_histograms(df.Sex.head(), df.Weight.head())