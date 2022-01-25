#!/usr/bin/python3
"""
    My addition module
"""


def add_integer(a, b=98):
    """ Addition function """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
    """ returns the sum of a and b """
