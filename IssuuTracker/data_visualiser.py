'''
created on: 16/11/2019-12:44
by: QDucasse
'''

import pandas            as pd
import seaborn           as sns
import matplotlib.pyplot as plt

class DataVisualiser():
    '''
    The DataVisualiser handles every plot from a given dataframe (countries,
    continents, etc.).
    Instance Variables
    ==================
    df: DataFrame
        Dataset that will be plotted by the DataVisualiser.
    '''
    def __init__(self,df):
        self.df = df

    def plot_feature(self,df,feature,xlabel,ylabel):
        '''
        Plot the number of the feature attribute in the given dataset.
        Parameters
        ==========
        df: Pandas.Dataframe
            Dataframe from which the feature is extracted.
        feature: string
            Feature to be extracted and shown.
        '''
        print(df.groupby(feature).size())
        plt.figure()
        sns.set(style="whitegrid", color_codes=True)
        hist = sns.countplot(x=feature,data=df)
        hist.set_xlabel(xlabel)
        hist.set_ylabel(ylabel)
        hist.tick_params(labelsize=5)
        plt.show()

    def plot_countries(self,df):
        '''
        Plot a histogram of the home countries of the visitors.
        Parameters
        ==========
        df: Pandas.DataFrame
            Dataframe extracted from the site.
        '''
        plot_feature(df,'visitor_country','Country','Count')

    def plot_continents(self,df):
        '''
        Plot a histogram of the home continents of the visitors.
        Parameters
        ==========
        df: Pandas.DataFrame
            Dataframe extracted from the site.
        '''
        plot_feature(df_cont,'visitor_continent','Continent','Count')

    def plot_browsers_verbose(self,df):
        '''
        Plot a histogram of the home continents of the visitors.
        Parameters
        ==========
        df: Pandas.DataFrame
            Dataframe extracted from the site.
        '''
        plot_feature(df,'visitor_useragent','Browser','Count')


    def plot_browsers(self,df):
        '''
        Plot a histogram of the home continents of the visitors.
        Parameters
        ==========
        df: Pandas.DataFrame
            Dataframe extracted from the site.
        '''
        plot_feature(df,'visitor_useragent_trimmed','Browser','Count')

if __name__ == "__main__":
    # IMPORTS TO TEST

    # TESTS OF THE DIFFERENT FUNCTIONS
