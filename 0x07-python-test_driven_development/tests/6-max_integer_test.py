#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        result = max_integer([1, 4, 6, 10])
        self.assertEqual(result, 10)
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))
    def test_single_element(self):
        self.assertEqual(max_integer([42]), 42)
    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
    def test_mixed_numbers(self):
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([-10, 20, -30, 40]), 40)

if __name__ == '__main__':
    unittest.main()
