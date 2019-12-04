'''
created on: 16/11/2019-12:44
by: QDucasse
'''
import matplotlib.pyplot as plt

class DataVisualiser():
    '''
    The DataVisualiser handles every plot from a given dataframe (countries,
    continents, etc.).
    Instance Variables
    ==================
    dicts: dictionary list
        Dictionaries loaded by a DataLoader.
    '''
    def __init__(self,dicts):
        self.dicts = dicts

    def create_histogram_dict(self,dicts,feature):
        '''
        Plot the number of the feature attribute in the given dataset.
        Parameters
        ==========
        dicts: dictionary list
            Dictionaries loaded by a DataLoader.
        feature: string
            Feature to be extracted and shown.

        Returns
        =======
        feature_dicts: dictionary
            Dictionary holding values as keys and count as values.
        '''
        feature_dict = {}
        for dict in dicts:
            if dict[feature] in feature_dict:
                feature_dict[dict[feature]] += 1
            else:
                feature_dict[dict[feature]] = 1
        return feature_dict

    def plot_feature(self,dicts,feature,xlabel,ylabel):
        '''
        Plot the number of the feature attribute in the given dataset.
        Parameters
        ==========
        dicts: dictionary list
            Dictionaries loaded by a DataLoader.
        feature: string
            Feature to be extracted and shown.
        xlabel: string
            Label of the X axis.
        ylabel: string
            Label of the Y axis.
        '''
        # CREATE HISTOGRAM DICT
        # =====================
        feature_dict = {}
        for dict in dicts:
            if dict[feature] in feature_dict:
                feature_dict[dict[feature]] += 1
            else:
                feature_dict[dict[feature]] = 1

        # PLOTTING
        # ========
        plt.figure()
        plt.bar(list(feature_dict.keys()),list(feature_dict.values()))
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.tick_params(labelsize=5)
        plt.show()

    def plot_countries(self,dicts=None):
        '''
        Plot a histogram of the home countries of the visitors.
        Parameters
        ==========
        dicts: Pandas.Dataframe
            Dataframe from which the feature is extracted.
        '''
        if dicts is None:
            dicts = self.dicts
        self.plot_feature(dicts,'visitor_country','Country','Count')

    def plot_continents(self,dicts=None):
        '''
        Plot a histogram of the home continents of the visitors.
        Parameters
        ==========
        dicts: dictionary list
            Dictionaries loaded by a DataLoader. Default None (instance variable)
        '''
        if dicts is None:
            dicts = self.dicts
        self.plot_feature(dicts,'visitor_continent','Continent','Count')

    def plot_browsers_verbose(self,dicts=None):
        '''
        Plot a histogram of the home continents of the visitors.
        Parameters
        ==========
        dicts: dictionary list
            Dictionaries loaded by a DataLoader. Default None (instance variable)
        '''
        if dicts is None:
            dicts = self.dicts
        self.plot_feature(dicts,'visitor_useragent','Browser','Count')


    def plot_browsers(self,dicts=None):
        '''
        Plot a histogram of the home continents of the visitors.
        Parameters
        ==========
        dicts: dictionary list
            Dictionaries loaded by a DataLoader. Default None (instance variable)
        '''
        if dicts is None:
            dicts = self.dicts
        self.plot_feature(dicts,'visitor_useragent_trimmed','Browser','Count')

if __name__ == "__main__":
    # IMPORTS TO TEST
    from IssuuTracker.data_loader import DataLoader,path_base_dataset
    dl_full = DataLoader()
    dl_full.complete_load(path_base_dataset)

    dv = DataVisualiser(dl_full.dicts)
    dv.plot_countries()
    dv.plot_continents()
    dv.plot_browsers()
