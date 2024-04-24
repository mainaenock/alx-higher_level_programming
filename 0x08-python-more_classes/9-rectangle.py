#!/usr/bin/python3
"""
This defines only a rectangle
"""


class Rectangle:
    """
    This is a class for the rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ initialization"""
        self.__width = width
        self.__height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        if not isinstance(self.__width, int):
            raise TypeError('width must be an integer')
        if self.__width < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if not isinstance(self.__height, int):
            raise TypeError('height must be an integer')
        if self.__height < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rec_str = ""
        for row in range(self.__height):
            rec_str += (str(self.print_symbol) * self.__width) + '\n'
        return rec_str.rstrip()

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("{}".format("Bye rectangle..."))
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        area1 = rect_1.width * rect_1.height
        area2 = rect_2.width * rect_2.height
        if area1 >= area2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
