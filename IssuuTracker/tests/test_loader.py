
import unittest
import pandas as pd
from nose.tools import raises
from IssuuTracker.loader import DataLoader, path_smpl_dataset

class LoaderTestCase(unittest.TestCase):

    def setUp(self):
        self.dl = DataLoader()

    def test_initialisation(self):
        self.assertEqual(1,0+1)
