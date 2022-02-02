#!/usr/bin/python3
""" Append to file module
"""


def append_write(filename="", text=""):
    """ appends to textfile and returns written bytes """
    with open(filename, mode='a', encoding='utf-8') as a_file:
        return a_file.write(text)
