#!/usr/bin/python3
"""
unit testing for square.py
"""


import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """
    class for testing square.py
    """


    def test_area(self):
        """
        tests for the area of a square
        """

        obj1 = Square(5)
        self.assertEqual(obj1.area(), 25)
