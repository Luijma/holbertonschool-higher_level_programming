#!/usr/bin/python3
""" Square Class Module
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class based on Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor for Square, calls Rectangle """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        rep = "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                        self.x,
                                                        self.y,
                                                        self.width)
        return rep
        """ Returns string rep of Square """

    @property
    def size(self):
        """ size getter """
        value = super().width
        return value
        """ gets size from parent getter """

    @size.setter
    def size(self, value):
        super(__class__, self.__class__).width.__set__(self, value)
