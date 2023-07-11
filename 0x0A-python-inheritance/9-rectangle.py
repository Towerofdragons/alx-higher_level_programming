#!/usr/bin/python3
"""
Module Defines the 'Rectangle class'
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Definition of the Rectangle class.
    """

    def __init__(self, width, height):
        self.integer_validator("height", height)
        self.integer_validator("width", width)

        self.__height = height
        self.__width = width

    def area(self):
        return(self.__height * self.__width)

    def __str__(self):
        return("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
