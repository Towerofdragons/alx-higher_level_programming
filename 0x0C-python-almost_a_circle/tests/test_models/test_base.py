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
    @classmethod
    def setUpClass(self):
        """
        Set up the first two instances of objects for use in testing Base class methods.
        """
        self.B1 = Base()
        self.R1 = Rectangle(1, 2)

    def test_to_json_string(self):
        """ Test 'Base' Static Method via inheritance with Rectangle subclass"""

        R1 = self.R1
        obj_list = []
        obj_list.append(R1.to_dictionary())
        self.assertEqual(R1.to_json_string(obj_list), '[{"id": 2, "width": 1, "height": 2, "x": 0, "y": 0}]')

    

    def test_id(self):
        """
        Test Automatic and manual assignment of instance Ids
        """
        self.assertEqual(1, self.B1.id)
        
        base2 = Base(3)

        self.assertEqual(3, base2.id)

    def test_obj_save_and_recover(self):
        """
        Test save to file method.
        """
        Instance = self.R1
        
        Instance.save_to_file([Instance])
        
        file_name = "Rectangle.json"
        with open(file_name, "r") as file:
            read_string = file.read()
        
        expected_string = '[{"id": 2, "width": 1, "height": 2, "x": 0, "y": 0}]'
        self.assertEqual(read_string, expected_string)

        


if __name__ == "__main__":
    unittest.main()
