#!/usr/bin/python3
""" inheritsfrom module
"""


def inherits_from(obj, a_class):
    """ checks if obj inherits from class
    """

    return ((type(obj) != a_class) and (issubclass(type(obj), a_class)))
