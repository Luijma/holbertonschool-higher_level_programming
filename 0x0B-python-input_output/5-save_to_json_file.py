#!/usr/bin/python3
""" writes json representatino to file
"""


import json


def save_to_json_file(my_obj, filename):
    """ saves json string representation of obj to file
    """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        a_file.write(json.dumps(my_obj))
