#!/usr/bin/python3
""" Module for creating obj from json files
"""


import json


def load_from_json_file(filename):
    """ creates object from json file
    """
    with open(filename, encoding='utf-8') as a_file:
        return json.load(a_file)
