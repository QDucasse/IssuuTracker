
import unittest
import pandas as pd
from nose.tools import raises
from IssuuTracker.data_loader import DataLoader, path_smpl_dataset

class LoaderTestCase(unittest.TestCase):

    def setUp(self):
        self.dl = DataLoader()
        self.dl.load_dataset_from('/Users/qducasse/Desktop/HWU/Industrial Programming/IP_CW2_DUCASSE/IssuuTracker/data/issuu_sample.json')

    def test_trimmed_browser_no_regex_match(self):
        # ARRANGE
        # =======
        # done in setup

        # ACT
        # ===
        test_dict = self.dl.dicts[-1]
        self.dl.add_trimmed_browser(test_dict)
        # ASSERT
        # ======
        self.assertEqual(test_dict['visitor_useragent_trimmed'],'P3P VALIDATOR')

    def test_load_dataset(self):
        dict_result1 = {   "ts": 1393631989,    "visitor_uuid": "745409913574d4c6",     "visitor_source": "external",    "visitor_device": "browser",    "visitor_useragent": "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_6 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B651 [FBAN/FBIOS;FBAV/7.0.0.17.1;FBBV/1325030;FBDV/iPhone4,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.0.6;FBSS/2; FBCR/Telcel;FBID/phone;FBLC/es_ES;FBOP/5]",    "visitor_ip": "0e1c9cd3d6c22c65",    "visitor_country": "MX",    "visitor_referrer": "ab11264107143c5f",    "env_type": "reader",    "env_doc_id": "140228202800-6ef39a241f35301a9a42cd0ed21e5fb0",       "event_type": "impression",    "subject_type": "doc",    "subject_doc_id": "140228202800-6ef39a241f35301a9a42cd0ed21e5fb0",    "subject_page": 23,    "cause_type": "page" }
        dict_result2 = {   "ts": 1393631989,    "visitor_uuid": "64bf70296da2f9fd",     "visitor_source": "internal",    "visitor_device": "browser",    "visitor_useragent": "P3P VALIDATOR",    "event_type": "pagereadtime",    "event_readtime": 797,    "subject_type": "doc",    "subject_doc_id": "130705172251-3a2a725b2bbd5aa3f2af810acf0aeabb",    "subject_page": 10}
        self.assertEqual(self.dl.dicts[0],dict_result1)
        self.assertEqual(self.dl.dicts[1],dict_result2)
