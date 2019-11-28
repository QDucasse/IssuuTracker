'''
created on: 16/11/2019-12:44
by: QDucasse
'''

import re

import pycountry_convert as pc
import pandas            as pd
import seaborn           as sns
import matplotlib.pyplot as plt
from collections import Counter

path_base_dataset = './data/issuu_cw2.json'
path_100k_dataset = './data/issu_100k.json'
path_400k_dataset = './data/issu_400k.json'
path_600k_dataset = './data/issu_600k.json'
path_3m_dataset = './data/issu_3m.json'
path_smpl_dataset = './data/issuu_sample.json'

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
    pattern = '([a-zA-Z]*)\/'
    trimmed_df = df
    trimmed_df['visitor_useragent'] = trimmed_df['visitor_useragent'].apply(lambda row: re.split(pattern,row)[1]+' '+re.split(pattern,row)[-2])
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
    return df.loc[df['subject_doc_id'] == doc_uuid, ['visitor_uuid','subject_doc_id']]

def readers_of_list(df,doc_uuid):
    '''
    Return the list of the readers of a document
    Parameters
    ==========
    Same as readers_of()

    Returns
    =======
    readers_list: string list
        List of the readers.
    '''
    return list(set(readers_of(df,doc_uuid)['visitor_uuid'].values.tolist()))

def has_read(df,visitor_uuid):
    '''
    Output the documents a user has read.
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
    return df.loc[df['visitor_uuid'] == visitor_uuid, ['visitor_uuid','subject_doc_id']]

def has_read_list(df,visitor_uuid):
    '''
    Output the list of documents a user has read.
    Parameters
    ==========
    Same as has_read()

    Returns
    =======
    readers_list: string list
        List of the documents.
    '''
    return list(set(has_read(df,visitor_uuid)['subject_doc_id'].values.tolist()))


def also_likes(df,doc_uuid,visitor_uuid=None,sort_func=None):
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
        Sort function to output the list ordered following this criteria.

    Returns
    =======
    df_list: Pandas.DataFrame list
        List of the dataframes read by other readers of the provided document.
    '''
    df_list = [docs for _,visitor in readers_of(df,doc_uuid)['visitor_uuid'].iteritems() for _,docs in has_read(df,visitor)['subject_doc_id'].iteritems()]
    if sort_func is None:
        return df_list
    else:
        return sort_func(df_list)

## SORTING FUNCTIONS
## =================

def sort_count_docs(docs_list):
    '''
    Sort the input list by frequency and remove duplicates.
    Parameters
    ==========
    docs_list: string list
        List of documents UUIDs.

    Returns
    =======
    sort_list: string list
        List of documents UUIDs sorted by frequency with no duplicates
    '''
    counts = Counter(docs_list)
    # Sorting by frequency
    sort_list = sorted(docs_list, key=counts.get, reverse=True)
    # Removing duplicates
    sort_list = list(set(sort_list))
    return sort_list



if __name__ == "__main__":
    full_df = load_dataset_json(path_base_dataset)
    smpl_df = load_dataset_json(path_smpl_dataset)
    plot_countries(full_df)
    plot_continents(full_df)
    plot_browsers_verbose(full_df)
    plot_browsers(full_df)
    print(readers_of(full_df,'130228184234-6fd07690237d48aaa7be4e20cb767b13'))
    print(has_read(full_df,'bd378ce6df7cb9cd'))
    print(also_likes(full_df,'120928161916-bbf9b86bb865460a8e674d5338115a18',sort_func=sort_count_docs))
