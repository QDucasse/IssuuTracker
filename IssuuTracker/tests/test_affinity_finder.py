import unittest
from IssuuTracker.data_loader     import DataLoader
from IssuuTracker.affinity_finder import AffinityFinder

class AffinityFinderTestCase(unittest.TestCase):

    def setUp(self):
        self.dl = DataLoader()
        self.dl.load_dataset_from('./data/tests/issuu_test_affinity_finder.json')
        self.af = AffinityFinder(self.dl.dicts)

    def list_equal(self,l1,l2):
        print(l1)
        print(l2)
        return len(l1)==len(l2) and sorted(l1)==sorted(l2)


    def test_readers_of(self):
        list_result = ["0000","1111"]
        readers_of = self.af.readers_of("aaaa")
        self.assertTrue(self.list_equal(list_result,readers_of))

    def test_has_read(self):
        list_result = ["aaaa","bbbb"]
        has_read = self.af.has_read("1111")
        self.assertTrue(self.list_equal(list_result,has_read))

    def test_also_likes_no_user(self):
        list_result = ["aaaa","bbbb"]
        also_likes = self.af.also_likes("aaaa")
        self.assertTrue(self.list_equal(list_result,also_likes))

    def test_also_likes_user0(self):
        list_result = ["aaaa","bbbb"]
        also_likes = self.af.also_likes("aaaa","0000")
        self.assertTrue(self.list_equal(list_result,also_likes))

    def test_also_likes_user1(self):
        list_result = ["bbbb"]
        also_likes = self.af.also_likes("bbbb","1111")
        self.assertTrue(self.list_equal(list_result,also_likes))
