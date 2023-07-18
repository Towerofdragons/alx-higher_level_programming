#!/usr/bin/python3
"""
Module defines class 'Square'.
"""


from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Square inherits from class 'Rectangle'
    """
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y ,id)

    @property
    def size(self):
       return self.__size
    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError ("width  must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.__size = size

    def update(self, *args, **kwargs):

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
        else:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v


    def to_dictionary(self):
        return {
                'x': self.x,
                'y': self.y,
                'id': self.id,
                'size': self.size
                }


    def __str__(self):
        return(f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")
