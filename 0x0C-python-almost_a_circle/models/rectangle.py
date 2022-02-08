#!/usr/bin/python3
""" Module for Rectangle
"""


from models.base import Base


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
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
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
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
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
        if (type(value) != int):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
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
        if (type(value) != int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        """ rectangle constructor """
        super().__init__(id)
        if (type(width) != int):
            raise TypeError("width must be an integer")
        if (type(height) != int):
            raise TypeError("height must be an integer")
        if (type(x) != int):
            raise TypeError("x must be an integer")
        if (type(y) != int):
            raise TypeError("y must be an integer")

        if (width <= 0):
            raise ValueError("width must be > 0")
        if (height <= 0):
            raise ValueError("height must be > 0")
        if (x < 0):
            raise ValueError("x must be >= 0")
        if (y < 0):
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def area(self):
        """ returns area of rectangle """
        return self.width * self.height
        """ Area of rectangle """

    def display(self):
        """ Displays rectangle in # """
        for row in range(self.height):
            for column in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """ returns string rep of rectangle """
        rep = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                self.x,
                                                                self.y,
                                                                self.width
                                                                self.height)

        return rep
        """ Returns string rep of Rectangle """
