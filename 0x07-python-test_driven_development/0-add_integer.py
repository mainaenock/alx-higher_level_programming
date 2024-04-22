#!/usr/bin/python3
"""
Adds 2 integers or floats
Args:a: first num
    b: second num
"""
def add_integer(a, b=98):
    """
    adds 2 integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
