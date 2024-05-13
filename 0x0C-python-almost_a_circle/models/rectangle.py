#!/usr/bin/python3
"""
class Rectangle that inherits from Base
"""


from models.base import Base


class Rectangle(Base):
    """
    inherits from super class Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): X-coordinat (default is 0).
            y (int, optional): Y-coordinate(default is 0).
            id (int, optional): Unique identifier (default is None).

        Attributes:
            __width (int): Private attribute for width.
            __height (int): Private attribute for height.
            __x (int): Private attribute for x-coordinate.
            __y (int): Private attribute for y-coordinate.
        """
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self):
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self):
        self.__y = y
