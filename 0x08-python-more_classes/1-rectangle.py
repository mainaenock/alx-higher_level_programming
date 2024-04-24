#!/usr/bin/python3
"""
This defines only a rectangle
"""


class Rectangle:
    """
    This is a class for the rectangle
    """
    def __init__(self, width=0, height=0):
        """ initialization"""
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        if not isinstance(self.__height, int):
            raise TypeError('height must be an integer')
        if self.__height < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if not isinstance(self.__width, int):
            raise TypeError('width must be an integer')
        if self.__width < 0:
            raise ValueError('width must be >= 0')
        self.__width = value
