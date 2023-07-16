#!/usr/bin/python3
"""
Unit test cases for class: Base
"""


import unittest
from models.base import Base

class Test_Base(unittest.TestCase):

    def test_id(self):
        base1 = Base()

        self.assertEqual(1, base1.id)
        
        base2 = Base(3)

        self.assertEqual(3, base2.id)


if __name__ == "__main__":
    unittest.main()
