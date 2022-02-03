#!/usr/bin/python3
""" Module for MyList class
"""


class MyList(list):
    """ My List class
    """

    def print_sorted(self):
        """ prints a sorted list
        """

        print(self.sort())
