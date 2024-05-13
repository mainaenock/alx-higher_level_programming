#!/usr/bin/python3
"""
testing rectangle.py
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle as rec
"""
imports the Rectangle module
"""


class TestRectangle(unittest.TestCase):
    """
    class for testing.
    """

    def test_equal(self):
        """
        test if the results are equal to the expected
        """
        obj1 = rec(10, 2)
        obj2 = rec(2, 10)

        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
    def test_custom(self):
        """
        tests if the custom id will reflect
        """

        obj3 = rec(1, 2, 3, 5, 12)

        self.assertEqual(obj3.id, 12)

    def test_errors(self):

        with self.assertRaises(TypeError):
            rec(10, "2")
        with self.assertRaises(TypeError):
            rec("eno", "2")
        with self.assertRaises(TypeError):
            rec(10, 4, "2")
        with self.assertRaises(TypeError):
            rec(10, 2, 5, "2")

        with self.assertRaises(ValueError):
            rec(10, -4)
        with self.assertRaises(ValueError):
            rec(1, 2, 3, -5)


if __name__ == "__main__":
    unittest.main()
