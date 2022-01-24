#!/usr/bin/python3
""" Module for the square class """


class Square:
    """ Square class description """
    __size = None
    __position = None

    def __init__(self, size=0, position=(0, 0)):
        """ docstring of __init__ method
        Args:
            size (int): size passed to constructor."""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        """ int: attribute with type specified"""
        if type(position) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """ docstring of area method. """
        return self.__size ** 2
    """ returns the size attribute with value """

    def my_print(self):
        """ my_print will print the square with # """
        if self.size != 0:
            for new_line in range(self.__position[1]):
                print("")
            for j in range(0, self.size):
                for spaces in range(0, self.__position[0]):
                    print(" ", end="")
                for i in range(0, self.size):
                    print("#", end="")
                print("")
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

    @property
    def position(self):
        """ Docstring of position getter """
        return self.__position
        """ returns the position attribute """

    @size.setter
    def position(self, value):
        """ Docstring of position

        Args:
            value (int): conatins position from __position atr """
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
