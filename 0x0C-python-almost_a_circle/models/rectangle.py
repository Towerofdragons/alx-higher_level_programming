#!/usr/bin/python3
"""
This module defines 'Rectangle' class (Inherits from base).
"""

from models.base import Base

class Rectangle(Base):
    """
    Defines the Rectangle class:
    Inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError ("width  must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError ("height must be an integer")
        if height <= 0:
            raise ValueError("height  must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError ("x must be an integer")

        if  x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError ("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y


    def area(self):
        """
        Returns area value of the rectangle instance.
        """
        return self.height * self.width

    def display(self):
        """
        Prints the rectangle to dimensions (height, width).
        Observes an offset to dimensions (x, y).
        """

        if self.y:
            for y in range(self.y):
                print()

        for h in range(self.height):
            if self.x:
                for x in range(self.x):
                    print(" ", end='')

            for w in range(self.width):
                print("#", end='')
            print()

    def __str__(self):
        return(f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}")

