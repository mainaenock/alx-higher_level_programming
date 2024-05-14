#!/usr/bin/python3
"""
this square inherits from Rectangle
"""


from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """
    this class inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        initialization of the square attributes
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size))
