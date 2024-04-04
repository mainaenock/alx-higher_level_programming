#!/usr/bin/python3

""" Define a class"""


class Square:

    """ __initialization__"""

    def __init__(self, size=0):

        """ init"""

        self.__size = size

    @property
    def size(self):
        """ getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError("size must be integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area"""
        return self.__size * self.__size
