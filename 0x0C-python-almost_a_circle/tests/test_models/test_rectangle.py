#!/usr/bin/python3
"""
Test module for class Rectangle.
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_id(self):
        base1 = Rectangle(3, 1, 0, 0, 1)

        self.assertEqual(1, base1.id)

        base2 = Rectangle(3, 5, 7, 0, 3)

        self.assertEqual(3, base2.id)

    def test_values(self):
        pass


if __name__ == "__main__":
    unittest.main()

