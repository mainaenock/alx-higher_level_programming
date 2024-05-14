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
        """
        this prints out the attributes in string format
        """
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, new_w):
        if not isinstance(new_w, int):
            raise TypeError("width must be an integer")
        elif new_w <= 0:
            raise ValueError("width must be > 0")
        self.width = new_w
        self.height = new_w

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.__x = args[2]
            if len(args) >= 4:
                self.__y = args[3]

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
