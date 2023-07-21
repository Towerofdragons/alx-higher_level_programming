#!/usr/bin/python3
"""
Unit test cases for class: Base
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class Test_Base(unittest.TestCase):
    """
    Tests attributes pertaining to the Base class.
    """

    def setUp(self):
        Main_Base_test_obj = Base()

    def test_to_json_string(self):
        """ Test 'Base' Static Method via inheritance with Rectangle subclass"""
        b1 = Base()

        R1 = Rectangle(1,3, id=2)
        l1 = []
        l1.append(R1.to_dictionary())
        self.assertEqual(b1.to_json_string(l1), '[{"id": 2, "width": 1, "height": 3, "x": 0, "y": 0}]')



    def test_id(self):
        base1 = Base(1)

        self.assertEqual(1, base1.id)
        
        base2 = Base(3)

        self.assertEqual(3, base2.id)

    def test_(self):
        pass


if __name__ == "__main__":
    unittest.main()
