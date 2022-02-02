#!/usr/bin/python3
""" MY READING FILE MODULE
"""


def read_file(filename=""):
    """ reads file and prints to screen """

    with open(filename, encoding='utf-8') as a_file:
        print("{}".format(a_file.read()))
