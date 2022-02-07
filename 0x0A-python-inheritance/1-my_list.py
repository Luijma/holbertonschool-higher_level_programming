#!/usr/bin/python3
""" Module for MyList class
"""


class MyList(list):
    """ My List class
    """

    def __init__(self):
        """ initiates list """
        super().__init__()

    def print_sorted(self):
        """ prints a sorted list
        """
        temp = self[:]
        temp.sort()
        print(temp)
