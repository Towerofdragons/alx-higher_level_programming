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

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        """Print square with #. """

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
