#!/usr/bin/python3
""" Module for the square class """


class Square:
    """ Square class description """
    __size = None

    def __init__(self, size=0):
        """ docstring of __init__ method
        Args:
            size (int): size passed to constructor."""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        """ int: attribute with type specified"""

    def area(self):
        """ docstring of area method. """
        return self.__size ** 2
    """ returns the size attribute with value """

    def my_print(self):
        """ my_print will print the square with # """
        i = 0
        j = 0
        if self.size != 0:
            while j < self.size:
                while i < self.size:
                    print("#", end="")
                    i += 1
                print("")
                j += 1
                i = 0
        else:
            print("")

    @property
    def size(self):
        """ Docstring of size getter """
        return self.__size
        """ returns the size attribute """

    @size.setter
    def size(self, value):
        """ Docstring of size

        Args:
            value (int): contains size from __size attribute """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
