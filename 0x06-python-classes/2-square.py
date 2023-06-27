#!/usr/bin/python3
""" Module contains class definition for the 'Square class'. """


class Square:
    """ Defines the attributes of a square."""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
