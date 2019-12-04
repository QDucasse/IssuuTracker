import unittest
from IssuuTracker.data_loader import DataLoader

class DataLoaderTestCase(unittest.TestCase):

    def setUp(self):
        self.dl = DataLoader()
        self.dl.load_dataset_from('./data/tests/issuu_test_data_loader.json')

    def test_load_dataset(self):
        dict_result1 = {"visitor_useragent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36","visitor_country":"MX"}
        dict_result2 = {"visitor_useragent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/540.36 (KHTML, like Gecko) Chrome/34.0.1750.112 Safari/538.36","visitor_country":"MX"}
        dict_result3 = {"visitor_useragent":"P3P Validator","visitor_country":"FR"}
        self.assertEqual(self.dl.dicts[0],dict_result1)
        self.assertEqual(self.dl.dicts[1],dict_result2)
        self.assertEqual(self.dl.dicts[2],dict_result3)

    def test_trimmed_browser_regex_match(self):
        test_dict = self.dl.dicts[0]
        self.dl.add_trimmed_browser(test_dict)
        self.assertEqual(test_dict['visitor_useragent_trimmed'],'Mozilla Safari')

    def test_trimmed_browser_no_regex_match(self):
        test_dict = self.dl.dicts[2]
        self.dl.add_trimmed_browser(test_dict)
        self.assertEqual(test_dict['visitor_useragent_trimmed'],'P3P Validator')

    def test_map_trim_browser(self):
        self.dl.map_trim()
        dict_result1 = {"visitor_useragent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36","visitor_country":"MX","visitor_useragent_trimmed":"Mozilla Safari"}
        dict_result2 = {"visitor_useragent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/540.36 (KHTML, like Gecko) Chrome/34.0.1750.112 Safari/538.36","visitor_country":"MX","visitor_useragent_trimmed":"Mozilla Safari"}
        dict_result3 = {"visitor_useragent":"P3P Validator","visitor_country":"FR","visitor_useragent_trimmed":"P3P Validator"}
        self.assertEqual(self.dl.dicts[0],dict_result1)
        self.assertEqual(self.dl.dicts[1],dict_result2)
        self.assertEqual(self.dl.dicts[2],dict_result3)

    def test_continent(self):
        test_dict1 = self.dl.dicts[0]
        test_dict2 = self.dl.dicts[2]
        self.dl.add_continent(test_dict1)
        self.dl.add_continent(test_dict2)
        self.assertEqual(test_dict1['visitor_continent'],'North America')
        self.assertEqual(test_dict2['visitor_continent'],'Europe')

    def test_map_add_continent(self):
        self.dl.map_continents()
        dict_result1 = {"visitor_useragent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36","visitor_country":"MX","visitor_continent":"North America"}
        dict_result2 = {"visitor_useragent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/540.36 (KHTML, like Gecko) Chrome/34.0.1750.112 Safari/538.36","visitor_country":"MX","visitor_continent":"North America"}
        dict_result3 = {"visitor_useragent":"P3P Validator","visitor_country":"FR","visitor_continent":"Europe"}
        self.assertEqual(self.dl.dicts[0],dict_result1)
        self.assertEqual(self.dl.dicts[1],dict_result2)
        self.assertEqual(self.dl.dicts[2],dict_result3)

    def test_complete_load(self):
        dl = DataLoader()
        dl.complete_load('./data/tests/issuu_test_data_loader.json')
        dict_result1 = {"visitor_useragent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36","visitor_country":"MX","visitor_useragent_trimmed":"Mozilla Safari","visitor_continent":"North America"}
        dict_result2 = {"visitor_useragent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/540.36 (KHTML, like Gecko) Chrome/34.0.1750.112 Safari/538.36","visitor_country":"MX","visitor_useragent_trimmed":"Mozilla Safari","visitor_continent":"North America"}
        dict_result3 = {"visitor_useragent":"P3P Validator","visitor_country":"FR","visitor_useragent_trimmed":"P3P Validator","visitor_continent":"Europe"}
        self.assertEqual(dl.dicts[0],dict_result1)
        self.assertEqual(dl.dicts[1],dict_result2)
        self.assertEqual(dl.dicts[2],dict_result3)
