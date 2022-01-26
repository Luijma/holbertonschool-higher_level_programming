#!/usr/bin/python3
"""Module for the rectangle class."""


class Rectangle:
    """Rectangle class description."""

    __width = None
    __height = None

    def __init__(self, width=0, height=0):
        """ constructor
        Args:
            width (int): width of rectangle.
            height (int): height of rectangle. """
        self.__width(width)
        self.__height(height)

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
        if (width < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.height
        """ returns height """

    @height.setter
    def height(self, value):
        """ height setter

        Args:
            value (int): contains width to assign """
        if (type(height) != int):
            raise TypeError("height must be an integer")
        if (height < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
