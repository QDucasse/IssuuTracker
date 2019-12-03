'''
created on: 28/11/2019-13:23
by: QDucasse
'''

import pandas as pd
from collections import Counter

class AffinityFinder():
    '''
    An AffinityFinder provides metrics on a given dataset and its instances.
    For example, it gives the readers of a certain document, the documents
    a reader has read and provides the "also likes" functionality (given
    a document, outputs the documents also read by readers of the first document)
    Instance Variables
    ==================
    df: DataFrame
        Dataset the metrics will be calculated on
    '''
    def __init__(self,df):
        self.df = df

    def readers_of(self,doc_uuid,df=None):
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
        if df is None:
            df = self.df
        return df.loc[df['subject_doc_id'] == doc_uuid, ['visitor_uuid','subject_doc_id']]

    def readers_of_list(self,doc_uuid,df=None):
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
        if df is None:
            df = self.df
        return list(set(self.readers_of(df,doc_uuid)['visitor_uuid'].values.tolist()))

    def has_read(self,visitor_uuid,df=None):
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
        if df is None:
            df = self.df
        return df.loc[df['visitor_uuid'] == visitor_uuid, ['visitor_uuid','subject_doc_id']]

    def has_read_list(self,visitor_uuid,df=None):
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
        if df is None:
            df = self.df
        return list(set(self.has_read(df,visitor_uuid)['subject_doc_id'].values.tolist()))


    def also_likes(self,doc_uuid,df=None,sort_func=None):
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
        if df is None:
            df = self.df
        df_list = [docs for _,visitor in self.readers_of(df,doc_uuid)['visitor_uuid'].iteritems() for _,docs in self.has_read(df,visitor)['subject_doc_id'].iteritems()]
        if sort_func is None:
            return df_list
        else:
            return sort_func(df_list)

    def also_likes_list(self,doc_uuid,df=None,sort_func=None):
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
        if df is None:
            df = self.df
        df_list = [docs for visitor in self.readers_of_list(df,doc_uuid) for docs in self.has_read_list(df,visitor)]
        if sort_func is None:
            return df_list
        else:
            return sort_func(df_list,doc_uuid)

    ## SORTING FUNCTIONS
    ## =================

    def sort_count_docs(self,docs_list,doc_uuid):
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
        sort_list.remove(doc_uuid)
        return sort_list

if __name__ == "__main__":
    # IMPORTS TO TEST
    from IssuuTracker.data_loader import DataLoader,path_base_dataset
    dl_full = DataLoader()
    dl_full.load_dataset_json(path_base_dataset)

    af = AffinityFinder(dl_full.df)
    print(af.also_likes_list('120928161916-bbf9b86bb865460a8e674d5338115a18'))
    # TESTS OF THE DIFFERENT FUNCTIONS
