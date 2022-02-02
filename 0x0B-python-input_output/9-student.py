#!/usr/bin/python3
""" Module for Student Class
"""


class Student:
    """ Defines a student
    """

    first_name = None
    last_name = None
    age = None

    def __init__(self, first_name, last_name, age):
        """ Student Constructor
        Args:
            first_name (str): name of student.
            last_name (str): student surname.
            age (int): student's age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
        """ returns the dict of the class """
