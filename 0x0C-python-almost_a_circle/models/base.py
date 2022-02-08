#!/usr/bin/python3
""" Base class
"""


class Base:
    """ Base Class for almost a circle project
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor for base class
        """

        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = __nb_objects
