#!/usr/bin/python3
"""Module for the rectangle class."""


class Rectangle:
    """Rectangle class description."""

    print_symbol = "#"
    number_of_instances = 0
    __height = None
    __width = None

    @property
    def height(self):
        """ height getter """
        return self.__height
        """ returns height """

    @height.setter
    def height(self, value):
        """ height setter

        Args:
            value (int): contains width to assign """
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ width getter """
        return self.__width
        """ returns width of attribute """

    @width.setter
    def width(self, value):
        """ width setter

        Args:
            value (int): contains width to assign """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    def __init__(self, width=0, height=0):
        """ constructor
        Args:
            width (int): width of rectangle.
            height (int): height of rectangle. """
        if (type(width) != int):
            raise TypeError("width must be an integer")
        if (width < 0):
            raise ValueError("width must be >= 0")
        if (type(height) != int):
            raise TypeError("height must be an integer")
        if (height < 0):
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1


    def area(self):
        """ area docstring """
        return self.height * self.width
        """ returns area of rectangle"""

    def perimeter(self):
        """ perimter docstring """
        if (self.height == 0 or
                self.width == 0):
            return 0
        return 2 * (self.height + self.width)
        """ returns perimeter """

    def __str__(self):
        """ returns representation of rectangle """
        rect = ""
        if (self.height == 0 or
                self.width == 0):
            return rect
        for row in range(self.height):
            for column in range(self.width):
                rect += str(self.print_symbol)
            if row == (self.height - 1):
                break
            rect += "\n"
        return rect

    def __repr__(self):
        """ returns visual representation of class """

        rep = ""
        rep += type(self).__name__
        rep += "({:d}, {:d})".format(self.width, self.height)

        return rep
        """ returns repr """

    def __del__(self):
        """ destructor for rectangle class """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
