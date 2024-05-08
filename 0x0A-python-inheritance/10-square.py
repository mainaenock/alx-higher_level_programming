#!/usr/bin/python3

"""
empty class
"""


class BaseGeometry:
    """
    An empty class
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name: str, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    child class
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """
        calculates the area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        prints
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    def __init__(self, size):
        self.__size = size
        super().__init__(size, size)
        self.integer_validator("size", self.__size)
