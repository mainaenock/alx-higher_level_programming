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
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_w):
        if not isinstance(new_w, int):
            raise TypeError("width must be an integer")
        elif new_w <= 0:
            raise ValueError("width must be > 0")
        self.__width = new_w

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_h):
        if not isinstance(new_h, int):
            raise TypeError("height must be an integer")
        elif new_h <= 0:
            raise ValueError("height must be > 0")
        self.__height = new_h

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new_x):
        if not isinstance(new_x, int):
            raise TypeError("x must be an integer")
        self.__x = new_x
        if new_x < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, new_y):
        if not isinstance(new_y, int):
            raise TypeError("y must be an integer")
        if new_y < 0:
            raise ValueError("y must be >= 0")
        self.__y = new_y

    def area(self):
        """
        returns are of Rectangle's instances
        """
        return self.__width * self.__height

    def display(self):
        """
        prints in stdout the Rectangle instance with the char #
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print("{}".format(" " * self.__x + '#' * self.__width))

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args):
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.__width = args[1]
        if len(args) >= 3:
            self.__height = args[2]
        if len(args) >= 4:
            self.__x = args[3]
        if len(args) >= 5:
            self.__y = args[4]
