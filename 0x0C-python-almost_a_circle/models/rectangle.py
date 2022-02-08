#!/usr/bin/python3
""" Module for Rectangle
"""

Base = __import__('base').Base

class Rectangle(Base):
    """ Rectangle Class for almost a circle """

    __width = None
    __height = None
    __x = None
    __y = None

    @property
    def width(self):
        """ width getter """
        return self.__width
        """ returns width """

    @width.setter
    def width(self, value):
        """ width setter

        Args:
            value (int): width of rectangle """

        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height
        """ returns height """

    @height.setter
    def height(self, value):
        """ height setter

        Args:
            value (int): height of rectangle """
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x
        """returns x """

    @x.setter
    def x(self, value):
        """ sets x

            Args:
                value (int): x var """
        self.__x = value

    @property
    def y(self):
        """ x getter """
        return self.__y
        """returns x """

    @y.setter
    def y(self, value):
        """ sets x

            Args:
                value (int): x var """
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        """ rectangle constructor """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
