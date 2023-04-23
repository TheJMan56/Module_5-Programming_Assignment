import unittest

from my_math import sum
from my_math import difference


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

class TestDifference(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can subtract a list of integers from a first number
        """
        data = [4, 2]
        result = difference(data)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
