#!/usr/bin/python3
"""
class inheriting list
"""


class MyList(list):
    """
    this is my class
    """
    def __init__(self):
        super().__init__(self)

    def print_sorted(self):
        """
       This method sorts the list
       """
        sorted_list = []
        for i in (self):
            if not isinstance(i, int):
                raise TypeError('contains non-integer')
        sorted_list = sorted(self)
        print("{}".format(sorted_list))
