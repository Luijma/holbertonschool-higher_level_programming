#!/usr/bin/python3
""" Base class
"""


import json


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
            self.id = Base.__nb_objects

    def to_json_string(list_dictoinaries):
        """ returns json representation of dictionaries
        """
        jstring = ""

        if (not list_dictionaries) or (list_dictionaries is None):
            return "[]"
        return json.dumps(list_dictionaries)
