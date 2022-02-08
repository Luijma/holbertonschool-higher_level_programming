#!/usr/bin/python3
""" Base Class Test Suite
"""


import unittest
Base = __import__("base").Base


class TestBaseClass(unittest.TestCase):
    """ Test Cases for base class
    """

    def test_1id_None(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_2id_None(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_id_NotNone(self):
        b1 = Base()
        b2 = Base(12)
        self.assertEqual(b2.id, 12)


if __name__ == '__main__':
    unittest.main()
