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
                                                        self.size)
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
        """ Sets size using rectangle's setter logic """
        super(__class__, self.__class__).width.__set__(self, value)
        super(__class__, self.__class__).height.__set__(self, value)

    def update(self, *args, **kwargs):
        """ calls rectangle's update """
        if (args) and (args is not None) and (len(args) > 0):
            attr = ["id", "size", "x", "y"]
            i = 0
            while (i < len(args)):
                setattr(self, attr[i], args[i])
                i += 1
        elif kwargs and kwargs is not None:
            super().update(**kwargs)
