import unittest

from my_math import difference


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
