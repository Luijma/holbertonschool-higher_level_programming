#!/usr/bin/python3
""" max_integer Test Suite """


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Test Cases for Max_integer function"""


    def test_max_at_end(self):
        numbers = [1, 2, 3, 4]
        self.assertEqual(max_integer(numbers), 4)

    def test_max_at_beginning(self):
        numbers = [4, 3, 2, 1]
        self.assertEqual(max_integer(numbers), 4)

    def test_max_in_middle(self):
        numbers = [3, 4, 2, 1]
        self.assertEqual(max_integer(numbers), 4)

    def test_one_negative_in_list(self):
        numbers = [-4, 4, 2, 1]
        self.assertEqual(max_integer(numbers), 4)

    def test_all_negative_in_list(self):
        numbers = [-1, -2, -3, -4]
        self.assertEqual(max_integer(numbers), -1)

    def test_one_element(self):
        numbers = [1]
        self.assertEqual(max_integer(numbers), 1)

    def test_empty_list(self):
        numbers = []
        self.assertEqual(max_integer(numbers), None)


if __name__ == '__main__':
    unittest.main()
