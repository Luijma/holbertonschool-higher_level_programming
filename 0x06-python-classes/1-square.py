#!/usr/bin/python3
""" Module for the square class """


class Square:
    """ Square class description """
    __size = None

    def __init__(self, size=0):
        """ docstring of __init__ method
        Args:
            size (int): size passed to constructor."""
        self.__size = size
        """ int: attribute with type specified"""
