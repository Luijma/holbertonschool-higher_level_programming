#!/usr/bin/python3
""" is_same_class module
"""


def is_same_class(obj, a_class):
    """ compares class names
    """

    if obj.__name__ == a_class.__name__:
        return True
    else:
        return False
