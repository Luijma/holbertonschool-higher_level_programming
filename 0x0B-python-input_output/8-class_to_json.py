#!/usr/bin/python3
""" returns dic description with simple data structure for json
"""


def class_to_json(obj):
    """ returns simple dictionary desc of object
    """
    return obj.__dict__
