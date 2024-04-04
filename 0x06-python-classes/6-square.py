#!/usr/bin/python3

""" Define a class"""


class Square:

    """ __initialization__"""

    def __init__(self, size=0, position=(0, 0)):

        """ init"""

        self.__size = size
        self.__position = position

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

    def my_print(self):
        for _ in range(self.__size):
            print("{}".format("#" * self.__size))

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(val, int) and val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
