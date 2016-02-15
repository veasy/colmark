import unittest
import urllib

__author__ = 'cansik'


class SimpleTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_call_main_page(self):
        res = -1
        try:
            res = urllib.urlopen("http://localhost:8000").getcode()
        except:
            pass

        self.assertEqual(200, res, "Colmark is down!")

if __name__ == '__main__':
    unittest.main()
