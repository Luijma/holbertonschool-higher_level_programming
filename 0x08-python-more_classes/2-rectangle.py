#!/usr/bin/python3
"""Module for the rectangle class."""


class Rectangle:
    """Rectangle class description."""

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

    def area(self):
        """ area docstring """
        return self.height * self.width
        """ returns area of rectangle"""

    def perimeter(self):
        """ perimter docstring """
        return 2 * (self.height * self.width)
        """ returns perimeter
