#!/usr/bin/python3
""" Module for file writing
"""


def write_file(filename="", text=""):
    """ writes text into file """

    with open(filename, mode='w', encoding='utf-8') as a_file:
        return a_file.write(text)
