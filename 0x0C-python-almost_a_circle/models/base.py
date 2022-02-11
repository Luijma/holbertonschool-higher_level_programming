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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns json representation of dictionaries
        """
        jstring = ""

        if (not list_dictionaries) or (list_dictionaries is None):
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes JSON rep of list_obj to file
        """

        filename = cls.__name__ + ".json"

        with open(filename, mode='w', encoding='utf-8') as a_file:
            if list_objs is None:
                a_file.write("[]")
            else:
                objects = [obj.to_dictionary() for obj in list_objs]
                a_file.write(cls.to_json_string(objects))
