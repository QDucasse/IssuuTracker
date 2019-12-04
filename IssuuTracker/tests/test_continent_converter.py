import unittest
from IssuuTracker.continent_converter import ContinentConverter

class ContinentConverterTestCase(unittest.TestCase):

    def setUp(self):
        self.cc = ContinentConverter()

    def test_key_found(self):
        self.assertEqual('Europe',self.cc.convert_country_alpha2_to_continent('FR'))

    def test_key_not_found(self):
        self.assertEqual('Undefined',self.cc.convert_country_alpha2_to_continent('ZZ'))
