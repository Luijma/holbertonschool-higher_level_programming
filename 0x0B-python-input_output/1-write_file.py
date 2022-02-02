#!/usr/bin/python3
""" Module for file writing
"""


def write_file(filename="", text=""):
    with open(filename, mode='w', encoding='utf-8') as a_file:
        a_file.write(text)
