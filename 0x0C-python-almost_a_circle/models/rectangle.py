#!/usr/bin/python3

"""Module defines Rectangle class."""

from models.base import Base

class Rectangle(Base):

    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError ("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError ("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError ("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError ("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value


    def update(self, *args, **kwargs):
        """Assigins new argument to each attribute"""
        lenth = len(args)
        if lenth and args != 0:
            if lenth >= 1:
                self.id = args[0]
            if lenth >= 2:
                self.width = args[1]
            if lenth >= 3:
                self.height = args[2]
            if lenth >= 4:
                self.x = args[3]
            if lenth >= 5:
                self.y = args[4]
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                if k == "width":
                    self.width = v
                if k == "height":
                    self.height = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v

    def area(self):
        """ Returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """prints the Rectnagle using """
        print("\n" * self.y, end="")
        for i in range(self.__height):
            print(" " * self.x, end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """Return the st nd prin repersention of Rectangle"""
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x,
                        self.y, self.width,
                        self.height))

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
