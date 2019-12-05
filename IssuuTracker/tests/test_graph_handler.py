import unittest
from IssuuTracker.data_loader   import DataLoader
from IssuuTracker.graph_handler import GraphHandler

class GraphHandlerTestCase(unittest.TestCase):

    def setUp(self):
        self.dl = DataLoader()
        self.dl.load_dataset_from('./data/tests/issuu_test_graph_handler.json')
        self.gh = GraphHandler(self.dl.dicts)

    def test_file_created(self):
        self.gh.create_graph(base_visitor_uuid="0000",base_document_uuid="aaaa",render=False)
        import os.path
        self.assertTrue(os.path.exists('graphs/alaaaa.dot'))
        self.assertTrue(os.path.exists('graphs/alaaaa.dot.pdf'))
