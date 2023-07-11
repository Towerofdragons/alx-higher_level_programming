#!/usr/bin/python3
"""
Module Defines the 'BaseGeometry class'
"""


class BaseGeometry:
    """
    Definition of the BaseGeometry class.
    """

    def area(self):
        """
        Defines how area is handled.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError ("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError ("{} must be greater than 0".format(name))
