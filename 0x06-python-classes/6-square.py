#!/usr/bin/python3
""" Module contains class definition for the 'Square class'. """


class Square:
    """ Defines the attributes of a square."""
    def __init__(self, size=0, position=(0,0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        self.position = position

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

        if self.position[1] > 0:
                print("\n" * self.position[1], end="")
        for i in range(self.__size):
            if self.position[0] > 0:
                print(" " * self.position[0], end="")
            print("#" * self.__size)

    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, value):
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len([val for val in value if (type(val) != int) and val >= 0]):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

