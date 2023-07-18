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
        super().__init__(size, size, x, y, id)


    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError ("width  must be an integer")
        if value < 0:
            raise ValueError("w must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigins new values to each respective attribute"""

        if args and len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.size = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]

        elif kwargs and len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                if k == "size":
                    self.size = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y}> - {self.width}"
