#!/usr/bin/python3

"""
Unit test cases for class: Square
"""

import unittest
from models.square import Square

class Test_Base(unittest.TestCase):

    def test_id(self):
        base1 = Square(2, 0, 0, 1)

        self.assertEqual(1, base1.id)

        base2 = Square(3, 5, 9, 3)

        self.assertEqual(3, base2.id)

    def test_values(self):
        pass


if __name__ == "__main__":
    unittest.main()
