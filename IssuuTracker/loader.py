'''
created on: 16/11/2019-12:44
by: QDucasse
'''

import pycountry_convert as pc
import pandas            as pd
import seaborn           as sns
import matplotlib.pyplot as plt

path_base_dataset = './data/issuu_cw2.json'
path_smpl_dataset = './data/issuu_sample.json'
path_cont_dataset = './data/country_continent.csv'

## LOADING DATASET
## ===============

def load_dataset_json(path):
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
    return df

## COLUMN OPERATIONS
## =================

def trim_browser(df):
    '''
    Trims the browser attribute.
    '''
    trimmed_df = df
    trimmed_df['visitor_useragent'] = trimmed_df['visitor_useragent'].apply(lambda row: row.split("/")[0])
    return trimmed_df

def get_continent_from_country_alpha2(country_code):
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
        return country_code
    else:
        return pc.country_alpha2_to_continent_code(country_code)

def add_continents(df):
    '''
    Add a 'visitor_continent' attribute determined by using the 'visitor_country'
    and linking it to the country_continent dataset.
    Parameters
    ==========
    df: Pandas.DataFrame
        Dataset extracted from the site.
    '''

    df_cont = df
    df_cont['visitor_continent'] = 'undefined'
    df_cont['visitor_continent'] = df_cont['visitor_country'].apply(lambda row: get_continent_from_country_alpha2(row))
    return df_cont

## VISUALISATION
## =============

def plot_feature(df,feature,xlabel,ylabel):
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
    graph = sns.countplot(x=feature,data=df)
    graph.set_xlabel(xlabel)
    graph.set_ylabel(ylabel)
    graph.tick_params(labelsize=5)
    plt.show()

def plot_countries(df):
    '''
    Plot a histogram of the home countries of the visitors.
    Parameters
    ==========
    df: Pandas.DataFrame
        Dataframe extracted from the site.
    '''
    plot_feature(df,'visitor_country','Country','Count')

def plot_continents(df):
    '''
    Plot a histogram of the home continents of the visitors.
    Parameters
    ==========
    df: Pandas.DataFrame
        Dataframe extracted from the site.
    '''
    df_cont = add_continents(df)
    plot_feature(df_cont,'visitor_continent','Continent','Count')

def plot_browsers_verbose(df):
    '''
    Plot a histogram of the home continents of the visitors.
    Parameters
    ==========
    df: Pandas.DataFrame
        Dataframe extracted from the site.
    '''
    plot_feature(df,'visitor_useragent','Browser','Count')


def plot_browsers(df):
    '''
    Plot a histogram of the home continents of the visitors.
    Parameters
    ==========
    df: Pandas.DataFrame
        Dataframe extracted from the site.
    '''
    trimmed_df = trim_browser(df)
    plot_browsers_verbose(trimmed_df)

## ALSO LIKES
## ==========

def readers_of(df,doc_uuid):
    '''
    Output the readers of a document given its uuid.
    Parameters
    ==========
    df: Pandas.DataFrame
        Dataframe extracted from the site.
    doc_uuid: string
        UUID of the document.

    Returns
    =======
    readers_list: Pandas.DataFrame
        Dataframe of the UUIDs of the readers of the given document.
    '''
    return df.loc[df['subject_doc_id']== doc_uuid, ['visitor_uuid']]

def has_read(df,visitor_uuid):
    '''
    Output the readers of a document given its uuid.
    Parameters
    ==========
    df: Pandas.DataFrame
        Dataframe extracted from the site.
    doc_uuid: string
        UUID of the document.

    Returns
    =======
    readers_list: Pandas.DataFrame
        Dataframe of the UUIDs of the readers of the given document.
    '''
    return df.loc[df['visitor_uuid']== visitor_uuid, ['sunject_doc_uuid']]

def also_likes(df,doc_uuid,visitor_uuid,sort_func):
    '''
    Output documents that have been read by the same visitors that read <doc_uuid>.
    Parameters
    ==========
    df: Pandas.DataFrame
        Dataset extracted from the site.
    doc_uuid: string
        UUID of the document.
    visitor_uuid: string
        (OPTIONAL) UUID of the visitor.
    sort_func: function

    Returns
    =======
    '''
    return

if __name__ == "__main__":
    full_df = load_dataset_json(path_base_dataset)
    smpl_df = load_dataset_json(path_smpl_dataset)
    # plot_countries(full_df)
    # plot_continents(full_df)
    # plot_browsers_verbose(full_df)
    # plot_browsers(full_df)
    # print(readers_of(full_df,'130228184234-6fd07690237d48aaa7be4e20cb767b13'))
