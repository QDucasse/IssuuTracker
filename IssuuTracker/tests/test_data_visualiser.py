import unittest
from IssuuTracker.data_loader     import DataLoader
from IssuuTracker.data_visualiser import DataVisualiser

class DataVisualiserTestCase(unittest.TestCase):

    def setUp(self):
        self.dl = DataLoader()
        self.dl.complete_load('./data/tests/issuu_test_data_visualiser.json')
        self.dv = DataVisualiser(self.dl.dicts)

    def test_histogram_countries(self):
        country_dict = self.dv.create_histogram_dict(self.dv.dicts,'visitor_country')
        dict_result = {'MX':2,'FR':1}
        self.assertEqual(country_dict,dict_result)

    def test_histogram_continents(self):
        cont_dict = self.dv.create_histogram_dict(self.dv.dicts,'visitor_continent')
        dict_result = {'North America':2,'Europe':1}
        self.assertEqual(cont_dict,dict_result)

    def test_histogram_browsers_verbose(self):
        vbrowsers_dict = self.dv.create_histogram_dict(self.dv.dicts,'visitor_useragent')
        dict_result = {
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36':1,
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/540.36 (KHTML, like Gecko) Chrome/34.0.1750.112 Safari/538.36':1,
            'P3P Validator':1
        }
        self.assertEqual(vbrowsers_dict,dict_result)

    def test_histogram_browsers_trimmed(self):
        tbrowsers_dict = self.dv.create_histogram_dict(self.dv.dicts,'visitor_useragent_trimmed')
        dict_result = {'Mozilla Safari':2,'P3P Validator':1}
        self.assertEqual(tbrowsers_dict,dict_result)
