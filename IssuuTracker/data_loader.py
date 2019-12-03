'''
created on: 16/11/2019-12:44
by: QDucasse
'''

import re
import pandas as pd
from IssuuTracker.continent_converter import ContinentConverter

path_smpl_dataset = './data/issuu_sample.json'
path_base_dataset = './data/issuu_cw2.json'
path_100k_dataset = './data/issu_100k.json'
path_400k_dataset = './data/issu_400k.json'
path_600k_dataset = './data/issu_600k.json'
path_3m_dataset   = './data/issu_3m.json'


class DataLoader():
    '''
    DataLoader is the wrapper around pandas in order to load datasets and perform
    operations on the columns (trimming the user_agent field, adding continents).
    Instance Variables
    ==================
    cconv: ContinentConverter
        Converter used for the transformation between countries and continents.
    df: DataFrame
        Dataset the DataLoader will load and perform operation on.
    '''
    def __init__(self):
        self.cconv = ContinentConverter()
        self.df = pd.DataFrame()

    def load_dataset_json(self,path):
        '''
        Load the .json dataset located at <path> in a pandas dataframe.
        Parameters
        ==========
        path: string
            Path of the dataset.

        Returns
        =======
        df: Pandas.DataFrame
            Dataframe of the dataset.
        '''
        df = pd.read_json(path,lines=True)
        self.df = df
        return df

    ## COLUMN OPERATIONS
    ## =================

    def trim_browser(self,df=None):
        '''
        Trims the browser attribute.
        '''
        if df is None:
            df = self.df
        pattern = '([a-zA-Z]*)\/'
        df['visitor_useragent_trimmed'] = df['visitor_useragent'].apply(lambda row: re.findall(pattern,row)[0]+' '+re.findall(pattern,row)[-1])
        return df

    def get_continent_from_country_alpha2(self,country_code):
        '''
        Wrapper of the pyconvert_country function to handle the 'ZZ' code case and
        return the same code (undefined) for the continent.
        Parameters
        ==========
        country_code: string
            Alpha 2 country code (ex. UK, FR, etc.)

        Returns
        =======
        continent: string
            Alpha 2 continent code (ex. NA, EU, etc.)
        '''
        undefined_country_codes = ['EU','ZZ','AP']
        if country_code in undefined_country_codes:
            return 'Undefined'
        else:
            return self.cconv.convert_country_alpha2_to_continent(country_code)

    def add_continents(self,df=None):
        '''
        Add a 'visitor_continent' attribute determined by using the 'visitor_country'
        and linking it to the country_continent dataset.
        Parameters
        ==========
        df: Pandas.DataFrame
            Dataset extracted from the site.
        '''
        if df is None:
            df = self.df
        df['visitor_continent'] = df['visitor_country'].apply(lambda row: self.get_continent_from_country_alpha2(row))
        return df

    def complete_load(self,path):
        self.load_dataset_json(path)
        self.trim_browser()
        self.add_continents()

if __name__ == "__main__":
    dl_full = DataLoader()
    dl_full.complete_load(path_base_dataset)



    dl_smpl = DataLoader()
    dl_smpl.complete_load(path_smpl_dataset)

    # smpl_df = load_dataset_json(path_smpl_dataset)
    # df_100k = load_dataset_json(path_100k_dataset)
    # df_400k = load_dataset_json(path_400k_dataset)
    # df_600k = load_dataset_json(path_600k_dataset)
    # df_3m = load_dataset_json(path_3m_dataset)

    # plot_countries(full_df)
    # plot_continents(full_df)
    # plot_browsers_verbose(smpl_df)
    # plot_browsers(full_df)
    # print(readers_of(full_df,'130228184234-6fd07690237d48aaa7be4e20cb767b13'))
    # print(readers_of_list(full_df,'130228184234-6fd07690237d48aaa7be4e20cb767b13'))
    # print(readers_of_list(full_df,'120928161916-bbf9b86bb865460a8e674d5338115a18'))
    # print(has_read(full_df,'bd378ce6df7cb9cd'))
    # print(has_read_list(full_df,'bd378ce6df7cb9cd'))
    # print(also_likes(full_df,'120928161916-bbf9b86bb865460a8e674d5338115a18',sort_func=sort_count_docs))

    # print(has_read_list(full_df,'2f63e0cca690da91'))
    # sprint(also_likes_list(full_df,'140219141540-c900b41f845c67cc08b58911155c681c',sort_func=sort_count_docs))

    # TEST REGEX
    # str = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36'
    # pattern = '([a-zA-Z]*)\/'
    # match = re.findall(pattern,str)
    # print(match)
    # print(dl_full.df.loc[dl_full.df['visitor_useragent_trimmed'] == 'Mozilla Mozilla', ['visitor_useragent']])
