#!/usr/bin/python3
""" deserializes string
"""


import json


def from_json_string(my_str):
    """ returns json deserialization
    """
    return json.loads(my_str)
