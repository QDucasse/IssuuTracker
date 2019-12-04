'''
created on: 01/12/2019-14:32
by: QDucasse
'''

import re
from IssuuTracker.continent_converter import ContinentConverter

path_smpl_dataset = './data/issuu_sample.json'
path_base_dataset = './data/issuu_cw2.json'
path_100k_dataset = './data/issuu_100k.json'
path_400k_dataset = './data/issuu_400k.json'
path_600k_dataset = './data/issuu_600k.json'
path_3m_dataset   = './data/issuu_3m.json'

class DataLoader():
    '''
    DataLoader is parser of files containing a list of dictionaries. It provides
    function to operate on certain fields of the dictionaries (adding a continent
    field from the country or trimming the user_agent field).
    Instance Variables
    ==================
    cconv: ContinentConverter
        Converter used for the transformation between countries and continents.
    dicts: dictionary list
        Dictionaries loaded by a DataLoader.
    '''
    def __init__(self):
        self.cconv = ContinentConverter()
        self.dicts = []

    def load_dataset_from(self,path):
        '''
        Load the list of dictionaries from a given path, store the list in the
        dicts instance variable.
        Parameters
        ==========
        path: string
            Path of the dataset.
        '''
        with open(path,'r') as file:
            for line in file:
                self.dicts.append(eval(line))

    # BROWSER OPERATIONS
    # ==================

    def add_trimmed_browser(self,dict):
        '''
        Add the field 'visitor_useragent_trimmed' to a given dictionary. The value
        of the field is calculated from the 'visitor_useragent' with a regex.
        Parameters
        ==========
        dict: dictionary
            One dictionary of the dataset.

        Returns
        =======
        new_dict: dictionary
            Given dictionary with a new field 'visitor_useragent_trimmed'
        '''
        pattern = '([a-zA-Z]*)\/'

        if 'visitor_useragent' in dict:
            browser_verbose = dict['visitor_useragent']
            if re.match(pattern,browser_verbose):
                dict['visitor_useragent_trimmed'] = re.findall(pattern,browser_verbose)[0]+' '+re.findall(pattern,browser_verbose)[-1]
            else:
                dict['visitor_useragent_trimmed'] = dict['visitor_useragent']
        return dict

    def map_trim(self,dicts=None):
        '''
        Perform the method add_trimmed_browser on all dictionaries present in the
        dicts instance variable.
        Parameters
        ==========
        dicts: dictionary list
            List of the dictionaries in the file. Default None (instance variable)
        '''
        if dicts is None:
            dicts = self.dicts
        dicts_with_trim = [self.add_trimmed_browser(dict) for dict in self.dicts]
        self.dicts = dicts_with_trim

    # COUNTRY/CONTINENT OPERATIONS
    # ============================
    def add_continent(self,dict):
        '''
        Add the field 'visitor_continent' to a given dictionary. The value
        of the field is calculated from the 'visitor_country' with the
        continent_converter.
        Parameters
        ==========
        dict: dictionary
            One dictionary of the dataset.

        Returns
        =======
        new_dict: dictionary
            Given dictionary with a new field 'visitor_useragent_trimmed'
        '''
        if 'visitor_country' in dict:
            dict['visitor_continent'] = self.cconv.convert_country_alpha2_to_continent(dict['visitor_country'])
            return dict

    def map_continents(self,dicts=None):
        '''
        Perform the method add_continent on all dictionaries present in the
        dicts instance variable.
        Parameters
        ==========
        dicts: dictionary list
            List of the dictionaries in the file. Default None (instance variable)
        '''
        if dicts is None:
            dicts = self.dicts
        dicts_with_cont = [self.add_continent(dict) for dict in self.dicts]
        self.dicts = dicts_with_cont

    def complete_load(self,path):
        '''
        Load the files and perform both additions (trimmed user agent and continent)
        on every dictionary.
        '''
        self.load_dataset_from(path)
        self.map_trim()
        self.map_continents()


if __name__ == "__main__":
    dl_base = DataLoader()
    dl_base.complete_load(path_base_dataset)
