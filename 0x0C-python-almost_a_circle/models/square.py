#!/usr/bin/python3
"""
Module defines class 'Square'
"""


from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Square inherits from class 'Rectangle'
    """

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)


    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError ("width  must be an integer")
        if value < 0:
            raise ValueError("w must be > 0")
        self.__width = value
        self.__height = value


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError ("x  must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError ("y  must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

