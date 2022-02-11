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

    @staticmethod
    def from_json_string(json_string):
        """ loads json string into object
        """

        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ creates instance with attributes set
        """
        temp = cls(**dictionary)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """ returns instances list
        """
        filename = cls.__name__ + ".json"
        instances = []

        try:
            with open(filename, "r", encoding="utf-8") as a_file:
                json_strings = cls.from_json_string(a_file.read())
                for items in json_strings:
                    instances.append(cls.create(**items))
        except FileNotFoundError:
            pass
        return instances
