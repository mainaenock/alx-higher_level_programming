#!/usr/bin/python3
"""
This is a unit testing file for the Base class
"""


import unittest
from base import Base


class TestBase(unittest.TestCase):
    """
    Class for unittest
    """

    
    obj1 = Base()
    obj2 = Base()
    obj3 = Base(id=7)
    obj4 = Base()
    def test_equal(self):
        """
        tests if the results and the expected results are equal
        """
        self.assertEqual(obj1, 1)
        self.assertEqual(obj2, 2)
        self.assertEqual(obj3, 7)
        self.assertEqual(obj4, 3)

if __name__ == "__main__":
    unittest.main()

