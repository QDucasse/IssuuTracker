'''
created on: 28/11/2019-13:23
by: QDucasse
'''

from collections import Counter

class AffinityFinder():
    '''
    An AffinityFinder provides metrics on a given dataset and its instances.
    For example, it gives the readers of a certain document, the documents
    a reader has read and provides the "also likes" functionality (given
    a document, outputs the documents also read by readers of the first document)
    Instance Variables
    ==================
    dicts: dictionary list
        Dictionaries loaded by a DataLoader.
    '''
    def __init__(self,dicts):
        self.dicts = dicts

    def readers_of(self,doc_uuid,dicts=None):
        '''
        Return the list of the readers of a document given its uuid.
        Parameters
        ==========
        doc_uuid: string
            UUID of the document.
        dicts: dictionary list
            Dictionaries loaded by a DataLoader. Default value None (instance variable).

        Returns
        =======
        readers_list: string list
            List of the UUIDs of the readers of the given document.
        '''
        if dicts is None:
            dicts = self.dicts
        return list(set([dict['visitor_uuid'] for dict in dicts if(('subject_doc_id' in dict) and ('visitor_uuid' in dict) and (dict['subject_doc_id']==doc_uuid))]))


    def has_read(self,visitor_uuid,dicts=None):
        '''
        Return the list of the documents read by a visitor given its uuid.
        Parameters
        ==========
        visitor_uuid: string
            UUID of the user.
        dicts: dictionary list
            Dictionaries loaded by a DataLoader. Default value None (instance variable).

        Returns
        =======
        read_documents_list: string list
            List of the UUIDs of the documents the visitor has read.
        '''
        if dicts is None:
            dicts = self.dicts
        return list(set([dict['subject_doc_id'] for dict in dicts if(('visitor_uuid' in dict) and ('subject_doc_id' in dict) and (dict['visitor_uuid']==visitor_uuid))]))

    def also_likes(self,doc_uuid,visitor_uuid=None,dicts=None,sort_func=None):
        '''
        Return the list of documents that have been read by the same visitors
        that read the given document.
        Parameters
        ==========
        doc_uuid: string
            UUID of the document.
        visitor_uuid: string
            UUID of the visitor. Default value None (optional)
        sort_func: function
            Sort function to output the list ordered following this criteria.

        Returns
        =======
        also_likes_list: string list
            List of the UUIDs of the documents read by other readers of the provided document.
        '''
        if dicts is None:
            dicts = self.dicts
        if sort_func is None:
            sort_func = self.sort_10best
        dicts_list = [docs for visitor in self.readers_of(doc_uuid,dicts) for docs in self.has_read(visitor,dicts)]
        return sort_func(dicts_list,doc_uuid)

    ## SORTING FUNCTIONS
    ## =================

    def sort_10best(self,docs_list,doc_uuid):
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
        return [doc_uuid] + sort_list[:10]

if __name__ == "__main__":
    # IMPORTS TO TEST
    from IssuuTracker.data_loader import DataLoader,path_base_dataset,path_100k_dataset
    dl_full = DataLoader()
    dl_full.load_dataset_from(path_base_dataset)

    af = AffinityFinder(dl_full.dicts)

    # Test 1
    # print(af.readers_of_list('130228184234-6fd07690237d48aaa7be4e20cb767b13'))
    # print(af.has_read_list('bd378ce6df7cb9cd'))
    # print(af.also_likes_list('120928161916-bbf9b86bb865460a8e674d5338115a18'))

    # Test 2
    # print(has_read_list('2f63e0cca690da91'))
    # print(also_likes_list('140219141540-c900b41f845c67cc08b58911155c681c'))

    dl_100k = DataLoader()
    dl_100k.load_dataset_from(path_100k_dataset)
    af100k = AffinityFinder(dl_100k.dicts)
    print(af100k.also_likes_list('100806162735-00000000115598650cb8b514246272b5'))
    # print(af100k.readers_of_list('aaaaaaaaaaaa-00000000df1ad06a86c40000000feadbe'))
    # print(af100k.has_read_list('4108dc09bfe11a0c'))
