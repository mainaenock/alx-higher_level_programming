#!/usr/bin/python3
"""
define the function
"""


def inherits_from(obj, a_class):
    """
    function
    """
    if isinstance(obj, a_class) and type(obj) is not (a_class):
        return True
    else:
        return False
