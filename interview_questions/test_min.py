import unittest
from sort_list import *

input_list = [1,5,2,7,9,4,99]

class Tester(unittest.TestCase):
    def test_min(self):
        self.assertEqual(find_smallest(input_list),1)

    def test_second_min(self):
        self.assertEqual(find_second_smallest(input_list),2)


if __name__ == '__main__':
    unittest.main()