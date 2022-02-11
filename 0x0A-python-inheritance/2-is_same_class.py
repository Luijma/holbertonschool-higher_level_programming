#!/usr/bin/python3
""" is_same_class module
"""


def is_same_class(obj, a_class):
    """ compares class names
    """

    if (type(obj) == a_class):
        return True
    else:
        return False
