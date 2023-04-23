#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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


# In my own interpretation of the results, I had to create an instance of a type of object class from the unittest module.  Within the instance, I inserted data into the function that I was testing, which came from the __init__ script in the my_sum folder of the same directory as the test script.  Using a built-in method for the TestCase object class, I asserted that the output of the tested function would equal to a pre-specified and known value.  If the output equals the pre-specified known value in the assertion method, then the test has passed, because the actual output is the same as the expected output, which is assumed to be correct.  If the output does not equal the pre-specified known value in the assertion method, then the test has failed, because the actual output is not the same as the expected output, which is assumed to be correct.
# 
# Multiple tests can be performed all at once, as long as each test script follows a “test_” naming convention.  When multiple tests are performed all at once, the user is told how many tests failed.  The failed tests are directly mentioned in the output of the terminal when multiple tests are performed all at once.  The exact line of code that produced the failure, which is the line that contains the use of the assertion method, is also directly mentioned in the terminal output.  The AssertionError is specified, with the actual output not equaling the asserted output.
# 
# My tests have passed, because the tested functions produce output that matches the expected output, which is assumed to be correct.
# 
